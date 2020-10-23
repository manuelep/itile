# -*- coding: utf-8 -*-

from . import settings
from .callbacks import get_image as get_image_
from .common import db

from py4web import action, redirect, URL, response, HTTP #, request, abort
# from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated

from kilimanjaro.frameworks.py4web.controller import brap

@action('itile/get/<name>/<zoom:int>/<xtile:int>/<ytile:int>', method=['GET'])
def itile(name, zoom, xtile, ytile):
    # response.headers['Content-Type'] = 'image/png'
    try:
        abs_img_path = get_image_(name=name, x=xtile, y=ytile, z=zoom)
    except KeyError:
        raise HTTP(404)
    else:
        rel_img_path = abs_img_path[len(db.image.file.uploadfolder):]
        url = URL(settings.IMAGE_ROOT, f"{settings.IMAGE_FOLDER}{rel_img_path}")
        db.commit()
        redirect(url)
