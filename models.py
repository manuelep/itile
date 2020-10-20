# -*- coding: utf-8 -*-

from .common import db, Field, tile_path
import datetime

now = lambda : datetime.datetime.utcnow()

db.define_table("image",
    Field("name"),
    Field("x"),
    Field("y"),
    Field("z"),
    Field("file", uploadseparate=True, uploadfolder=tile_path),
    Field("uid", notnull=True, unique=True,
        compute = lambda row: "{name}.{x}.{y}.{z}".format(**row)
    ),
    Field('created_on', 'datetime',
        default = now,
        writable=False, readable=False,
        label = 'Created On'
    ),
    Field('modified_on', 'datetime',
        update=now, default=now,
        writable=False, readable=False,
        label = 'Modified On'
    )
)
