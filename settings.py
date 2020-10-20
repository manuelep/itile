# -*- coding: utf-8 -*-

import os

CHECK_TILE_PATH = True

STYLE_FOLDER = 'resources'
STYLE_PATH = os.path.join(os.path.dirname(__file__), STYLE_FOLDER)

DEFAULT_STYLE = os.path.join(STYLE_PATH, 'postgis-default-styles.xml')

LAYER_CONF = {
    # How to compile this variable in your private settings:
    # "[UNIQUE NAME (VIEW/TABLE NAME ITS FINE)]": {
    #     "parameters": {
    #         NOTE: At the moment the only one supported
    #         "driver": "postgis",
    #         "host": "[HOST]",
    #         "dbname": "[DB NAME]",
    #         "user": "[USERNAME]",
    #         "password": "[USER PASSOWRD]",
    #         "extent": "-180,-85.05113,180,85.05113"
    #     },
    #     "queries": {
    #         "[QUERY OR VIEW/TABLE NAME]": "[STYLE NAME]"
    #     }
    # }
}

IMAGE_ROOT = 'static'
IMAGE_FOLDER = 'tiles'

IMAGE_CACHE = 3600

APP_FOLDER = os.path.dirname(os.path.dirname(__file__))
DB_URI = "sqlite://storage.db"
DB_POOL_SIZE = 10
DB_MIGRATE = True
DB_FOLDER = os.path.join(APP_FOLDER, "databases")
DB_FAKE_MIGRATE = False

# try import private settings
try:
    from .settings_private import *
except ModuleNotFoundError:
    pass
