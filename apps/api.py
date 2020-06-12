# -*- coding: utf-8 -*-

# Import
from flask_restful import Api, Resource
from apps.collaborators.services import CollaboratorsList

# Instance of FlaskRestful API
api = Api()


def configure_api(app):
    
    # Collaborators routes
    api.add_resource(CollaboratorsList, '/collaborators')
    
    # Initialize api with settings came from app
    api.init_app(app)