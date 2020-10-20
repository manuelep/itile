#!/usr/bin/env python

from . import settings
from .common import mymaps, tile_path
from .models import db, now

def get_img(name, x, y, z):
    stream = mymaps[name].tile(x, y, z)
    uname = db.image.uid.compute(dict(name=name, x=x, y=y, z=z))
    filename = f"{uname}.png"
    return stream, filename,


def get_image(name, x, y, z):
    rec = db.image(name=name, x=x, y=y, z=z)
    if rec is None:
        stream, filename = get_img(name, x, y, z)
        newid = db.image.insert(
            name=name, x=x, y=y, z=z,
            file = db.image.file.store(stream, filename)
        )
        rec = db.image[newid]
    elif (now() - rec.modified_on).seconds > settings.IMAGE_CACHE:
        stream, filename = get_img(name, x, y, z)
        rec.update_record(file = db.image.file.store(stream, filename))

    _, path_to_img = db.image.file.retrieve(rec.file, nameonly=True)
    return path_to_img

if __name__=='__main__':
    import pdb; pdb.set_trace()
