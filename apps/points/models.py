# Python
from datetime import datetime

# Third
from mongoengine import StringField

# Apps
from apps.db import db
from apps.collaborators.models import CollaboratorBase


class Point(CollaboratorBase):

    """
    Default implementation for point fields
    """
    meta = {
        'collection': 'points'
    }
    date = StringField(required=True, default='')
    time = StringField(required=True, default='')
