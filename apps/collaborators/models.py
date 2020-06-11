# Python
from datetime import datetime

# Third
from mongoengine import (
    DateTimeField,
    EmailField,
    StringField,
)

# Apps
from apps.db import db

class Collaborator(db.Document):
    
    '''
    Collaborator
    '''
    
    meta = {'collection': 'collaborators'}

    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    cpf = StringField(default='')
    rf = StringField(required=True, default='')
    created = DateTimeField(default=datetime.now)
