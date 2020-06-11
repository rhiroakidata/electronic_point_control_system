# -*- coding: utf-8 -*-

# Import
from flask_restful import Api, Resource

# Instance of FlaskRestful API
api = Api()


def configure_api(app):
    
    # Initialize api with settings came from app
    api.init_app(app)