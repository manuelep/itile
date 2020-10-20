# -*- coding: utf-8 -*-

import mapnik
import mercantile
import os
import png
import math
import io
from PIL import Image

from .settings import *

def _get_max_width_and_heigth(styles):
    """ Parses layer styles and return max symbol width and height """

    def _loopOstyles():
        for style_name, style in styles:
            for rule in style.rules:
                for _symbol in rule.symbols:
                    symbol = _symbol.extract()
                    yield symbol.width, symbol.height

    W, H = 0, 0
    for w,h in _loopOstyles():
        if w and w>W:
            W = w
        if h and h>H:
            H = h

    return int(W)+1, int(H)+1

def newmap(deltaw=0, deltah=0, width=256, height=256, stylesheet=DEFAULT_STYLE):
    mymap = mapnik.Map(width+deltaw, height+deltah)
    mapnik.load_map(mymap, stylesheet)
    # mymap.buffer_size = 20
    mymap.aspect_fix_mode = mapnik._mapnik.aspect_fix_mode.RESPECT
    return mymap


class _MapWrapper_(object):
    """ """

    tile_width = 256
    tile_height = 256

    def __init__(self, stylesheet=DEFAULT_STYLE):
        # super(MapWrapper).__init__()
        self.map = newmap(stylesheet=stylesheet)

    def set_buffer_size(self):
        buffer = max(_get_max_width_and_heigth(self.map.styles))
        self.map.buffer_size = 2*buffer

    def render_tile(self, row, column, zoom, image_type='png'):
        dw = self.map.width-self.tile_width
        dh = self.map.height-self.tile_height

        bounds = mercantile.bounds(row, column, zoom)

        self.map.zoom_to_box(mapnik.Box2d(*bounds))

        image = mapnik.Image(self.map.width, self.map.height)
        mapnik.render(self.map,image)
        if image_type is None:
            return image.tostring()
        else:
            return image.tostring(image_type)

    def build_file(self, image_string):
        big_image = Image.frombytes("RGBA", (self.map.width, self.map.height), image_string)
        dw = self.map.width-self.tile_width
        dh = self.map.height-self.tile_height
        if any((dw, dh,)):
            image = big_image.crop((dw,dh,self.tile_width+dw,self.tile_height+dh,))
        else:
            image = big_image
        file = io.BytesIO()
        image.save(file, 'png')
        file.seek(0)
        return file

    @staticmethod
    def build_png_file(image_string):
        rr = png.Reader(bytes=image_string)
        return rr.file

    def tile(self, row, column, zoom, **__):
        return self.build_png_file(self.render_tile(*list(map(int, (row, column, zoom,)))))

    def tile2(self, row, column, zoom, **__):
        return self.build_file(
            self.render_tile(*list(map(int, (row, column, zoom,))), image_type=None)
        )


class MapPGWrapper(_MapWrapper_):
    """docstring for MapWrapper."""

    def __init__(self, name, *styles, stylesheet=DEFAULT_STYLE, **parameters):
        super(MapPGWrapper, self).__init__(stylesheet=stylesheet)
        layer = mapnik.Layer(name)
        # https://github.com/mapnik/mapnik/wiki/PostGIS
        layer.datasource = mapnik.PostGIS(**parameters)
        for style in styles:
            layer.styles.append(style)
        self.map.layers.append(layer)
        self.set_buffer_size()


class MapManager(dict):
    """docstring for MapManager."""

    drivers = {
        'postgis': MapPGWrapper
    }

    def new(self, layer_name, driver, table, styles, **pars):
        try:
            klass = self.drivers[driver]
        except KeyError:
            raise NotImplementedError('Driver {} not supported.'.format(driver))
        else:
            return klass(layer_name, *styles.split(','), table=table, **pars)

    def __init__(self, conf, stylesheet=DEFAULT_STYLE):
        super(MapManager, self).__init__()

        for _,connection in conf.items():
            for table, styles in list(connection['queries'].items()):
                self[table] = dict(table=table, styles=styles, stylesheet=stylesheet, **connection['parameters'])

    def __setitem__(self, name, val):
        dict.__setitem__(self, name, self.new(name, **val))

if __name__ == '__main__':
    import pdb; pdb.set_trace()
