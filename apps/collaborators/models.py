# Python
from datetime import datetime

# Third
from mongoengine import (
    DateTimeField,
    EmailField,
    StringField,
    IntField,
    BooleanField
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
    rf = IntField(required=True, default='')
    active = BooleanField(default=False)
    created = DateTimeField(default=datetime.now)
    
    def is_active(self):
        return self.active
