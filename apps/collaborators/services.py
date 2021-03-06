# -*- coding:utf-8 -*-

# Python
import random

# Flask
from flask import request

# Third
from flask_restful import Resource
from bcrypt import gensalt, hashpw
from mongoengine.errors import NotUniqueError, ValidationError
from mongoengine.errors import FieldDoesNotExist

# Apps
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok
)

from apps.messages import (
    MSG_RESOURCE_CREATED,
    MSG_RESOURCE_FETCHED_LISTED,
    MSG_RESOURCE_FETCHED,
    MSG_RESOURCE_DELETED,
    MSG_NO_DATA,
    MSG_PASSWORD_WRONG,
    MSG_INVALID_DATA
)

# Local
from .models import Collaborator
from .schemas import CollaboratorRegistrationSchema, CollaboratorSchema
from apps.utils import check_password_in_signup, get_collaborator_by_rf


class CollaboratorsServices(Resource):
    def post(self, *args, **kwargs):
        # Initialize variables
        #print(request.json)
        req_data = request.get_json(force=True) or None
        #print(req_data)
        data, errors, result = None, None, None
        password, confirm_password = None, None
        schema = CollaboratorRegistrationSchema()

        # When datas are null
        if req_data is None:
            return resp_data_invalid('CollaboratorsServices', [], msg=MSG_NO_DATA)

        password = req_data.get('password', None)
        confirm_password = req_data.pop('confirm_password', None)
        req_data['rf'] = random.randint(100000,999999)
        

        # Verify passwords provided
        if not check_password_in_signup(password, confirm_password):
            errors = {'password': MSG_PASSWORD_WRONG}
            return resp_data_invalid('CollaboratorsServices', errors)

        # Desserialize data
        data, errors = schema.load(req_data)

        # Return invalid response when there is a error
        if errors:
            return resp_data_invalid('CollaboratorsServices', errors)

        # Create hash
        hashed = hashpw(password.encode('utf-8'), gensalt(12))

        # Save the model. If get Exception, return JSON response.
        try:
            data['password'] = hashed
            data['email'] = data['email'].lower()
            model = Collaborator(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists('CollaboratorsServices', 'colaborador')

        except ValidationError as e:
            return resp_exception('CollaboratorsServices', msg=MSG_INVALID_DATA, description=e)

        except Exception as e:
            return resp_exception('CollaboratorsServices', description=e)

        # Dump data of model
        schema = CollaboratorSchema()
        result = schema.dump(model)

        return resp_ok(
            'CollaboratorsServices', MSG_RESOURCE_CREATED.format('Colaborador'),  data=result.data,
        )
    
    def get(self):
        # Initialize schema
        schema = CollaboratorSchema(many=True)
        
        try:
            # Fetch all collaborators
            collaborators = Collaborator.objects()

        except FieldDoesNotExist as e:
            return resp_exception('CollaboratorsServices', description=e.__str__())

        except Exception as e:
            return resp_exception('CollaboratorsServices', description=e.__str__())

        # Dump objects returned
        result = schema.dump(collaborators)

        return resp_ok(
            'CollaboratorsServices',
            MSG_RESOURCE_FETCHED_LISTED.format('colaboradores'),
            data=result.data
        )


class CollaboratorServices(Resource):
    
    def get(self, rf):
        result = None
        schema = CollaboratorSchema()

        collaborator = get_collaborator_by_rf(rf=rf)

        result = schema.dump(collaborator)

        return resp_ok(
            'ColaboratorServices',
            MSG_RESOURCE_FETCHED.format('Colaborador'),
            data=result.data
        )
        
    def delete(self, rf):
        # Fetch collaborator by rf
        collaborator = get_collaborator_by_rf(rf)

        if not isinstance(collaborator, Collaborator):
            return collaborator

        try:
            collaborator.active = False
            collaborator.save()

        except NotUniqueError:
            return resp_already_exists(
                        'CollaboratorServices',
                        'colaborador'
                    )

        except ValidationError as e:
            return resp_exception(
                        'CollaboratorServices',
                        msg=MSG_INVALID_DATA,
                        description=e.__str__()
                    )

        except Exception as e:
            return resp_exception(
                        'CollaboratorServices',
                        description=e.__str__()
                    )

        return resp_ok(
                    'CollaboratorServices',
                    MSG_RESOURCE_DELETED.format('Colaborador')
                )
