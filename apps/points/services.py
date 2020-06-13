# Python
from datetime import datetime
import json

# Flask
from flask import request

# Third
from flask_restful import Resource
from mongoengine.errors import (
    NotUniqueError,
    ValidationError,
    DoesNotExist,
    FieldDoesNotExist
)
from mongoengine.queryset.visitor import Q

# Apps
from apps.responses import (
    resp_already_exists,
    resp_does_not_exist,
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
from apps.utils import (
    get_collaborator_by_rf,
    get_point_by_rf_id
)

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

class PointServices(Resource):
    
    def get(self, rf, point_id):
        result = None
        schema = PointSchema()

        point = get_point_by_rf_id(rf=rf, point_id=point_id)
        
        if not isinstance(point, Point):
            return point

        result = schema.dump(point)

        return resp_ok(
            'PointServices',
            MSG_RESOURCE_FETCHED.format('Ponto'),
            data=result.data
        )
        
    def delete(self, rf, point_id):
        # Fetch point by rf
        point = get_point_by_rf_id(rf, point_id)

        if not isinstance(point, Point):
            return point

        try:
            point.active = False
            point.save()

        except ValidationError as e:
            return resp_exception(
                        'PointServices',
                        msg=MSG_INVALID_DATA,
                        description=e.__str__()
                    )

        except Exception as e:
            return resp_exception(
                        'PointServices',
                        description=e.__str__()
                    )

        return resp_ok(
                    'PointServices',
                    MSG_RESOURCE_DELETED.format('Ponto')
                )
        

class ReportService(Resource) :
    def get(self, rf, month_id):        
        try:
            # Fetch point by rf
            points = Point.objects(
                Q(date__contains=month_id) & Q(rf=rf)
            ).order_by('date')
            
        except DoesNotExist:
            return resp_does_not_exist('PointServices', 'ponto')

        except FieldDoesNotExist as e:
            return resp_exception('PointServices', description=e.__str__())

        except Exception as e:
            return resp_exception('PointServices', description=e.__str__())

        # It will be auxiliar for changing date
        # Convert string to datetime
        staticDate = datetime.strptime(points.first().date, '%Y-%m-%d').date()
        result = {}
        hoursPerDay = 0
        hoursPerMonth = 0
        for point in range(0, points.count()):
            date = datetime.strptime(
                points[point].date, '%Y-%m-%d'
            ).date()

            if (date != staticDate):
                staticDate = date
                hoursPerDay=0
            
            if point%2 == 0:
                punchIn = datetime.strptime(
                    points[point].time, '%H:%M:%S'
                ).hour
            else:
                punchOut = datetime.strptime(
                    points[point].time, '%H:%M:%S'
                ).hour

            if point%2 == 1:
                hoursPerDay = hoursPerDay + (punchOut-punchIn)
                
                # Take work hours per day,
                # Convert datetime to string
                result["Day " + date.strftime('%Y-%m-%d')] = hoursPerDay
                
                hoursPerMonth = hoursPerMonth + punchOut - punchIn
        
        result["Month " + month_id] = hoursPerMonth
        return resp_ok(
            'ReportService',
            MSG_RESOURCE_FETCHED.format('Relatorio'),
            result
        )
        