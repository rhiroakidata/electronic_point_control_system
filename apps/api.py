# -*- coding: utf-8 -*-

# Import
from flask_restful import Api, Resource
from apps.collaborators.services import (
    CollaboratorsServices,
    CollaboratorServices
)
from apps.points.services import (
    PointsServices,
    PointServices,
    ReportService
)

# Instance of FlaskRestful API
api = Api()


def configure_api(app):
    
    # Collaborators routes
    api.add_resource(CollaboratorsServices, '/collaborators')
    
    # Collaborator routes
    api.add_resource(CollaboratorServices, '/collaborators/<int:rf>')
    
    # Points routes
    api.add_resource(PointsServices, '/points')
    
    # Point routes
    api.add_resource(PointServices, '/points/<string:point_id>')
    
    # Report
    api.add_resource(ReportService, '/collaborators/<int:rf>/month/<string:month_id>')
    
    # Initialize api with settings came from app
    api.init_app(app)