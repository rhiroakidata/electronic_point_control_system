# -*- coding: utf-8 -*-

from flask import Flask
from config import config

from .db import db

from .api import configure_api


def create_app(config_name):

    app = Flask('api-pontotel')

    app.config.from_object(config[config_name])

    # Setup MongoEngine
    db.init_app(app)

    configure_api(app)

    return app