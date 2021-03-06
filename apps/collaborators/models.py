# Python
from datetime import datetime

# Third
from mongoengine import (
    DateTimeField,
    EmailField,
    StringField,
    IntField,
    BooleanField,
    EmbeddedDocumentField,
)

# Apps
from apps.db import db


class CollaboratorBase(db.Document):
    """
    Default implementation for Collaborator
    """
    meta = {
        'abstract': True
    }

    rf = IntField(required=True, default='')
    active = BooleanField(default=True)
    
    def is_active(self):
        return self.active


class Collaborator(CollaboratorBase):
    
    '''
    Collaborator
    '''
    
    meta = {'collection': 'collaborators'}

    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    cpf = StringField(default='')
    created = DateTimeField(default=datetime.now)
