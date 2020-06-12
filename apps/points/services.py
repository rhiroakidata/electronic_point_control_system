# Flask
from flask import request

# Third
from flask_restful import Resource
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
from apps.utils import get_collaborator_by_rf

# Local
from .models import Point
from .schemas import PointRegistrationSchema, PointSchema


class PointsServices(Resource):
    def post(self, *args, **kwargs):
        # Initialize variables
        req_data = request.get_json(force=True) or None

        data, errors, result = None, None, None
        schema = PointRegistrationSchema()

        # When datas are null
        if req_data is None:
            return resp_data_invalid('PointsServices', [], msg=MSG_NO_DATA)
        
        collaborator = get_collaborator_by_rf(rf=req_data['rf'])

        # Desserialize data
        data, errors = schema.load(req_data)

        # Return invalid response when there is a error
        if errors:
            return resp_data_invalid('PointsServices', errors)

        # Save the model. If get Exception, return JSON response.
        try:
            model = Point(**data)
            model.save()

        except ValidationError as e:
            return resp_exception('PointsServices', msg=MSG_INVALID_DATA, description=e)

        except Exception as e:
            return resp_exception('PointsServices', description=e)

        # Dump data of model
        schema = PointSchema()
        result = schema.dump(model)

        return resp_ok(
            'PointsServices', MSG_RESOURCE_CREATED.format('Ponto'),  data=result.data,
        )
        
    def get(self):
        # Initialize schema
        schema = PointSchema(many=True)
        
        try:
            # Fetch all points
            points = Point.objects()

        except FieldDoesNotExist as e:
            return resp_exception('PointsServices', description=e.__str__())

        except Exception as e:
            return resp_exception('PointsServices', description=e.__str__())

        # Dump objects returned
        result = schema.dump(points)

        return resp_ok(
            'PointsServices',
            MSG_RESOURCE_FETCHED_LISTED.format('pontos'),
            data=result.data
        )
