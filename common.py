# -*- coding: utf-8 -*-


import os
from pathlib import Path

from py4web import DAL, Field, request

from . import settings
from .core import MapManager

tile_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), settings.IMAGE_ROOT, settings.IMAGE_FOLDER)

if settings.CHECK_TILE_PATH:
    Path(tile_path).mkdir(parents=True, exist_ok=True)

mymaps = MapManager(settings.LAYER_CONF, stylesheet=settings.DEFAULT_STYLE)

# connect to db
db = DAL(
    settings.DB_URI,
    folder = settings.DB_FOLDER,
    pool_size = settings.DB_POOL_SIZE,
    migrate = settings.DB_MIGRATE,
    fake_migrate = settings.DB_FAKE_MIGRATE,
)
