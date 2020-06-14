from mongoengine.errors import FieldDoesNotExist, DoesNotExist

from apps.responses import resp_exception, resp_does_not_exist

from apps.collaborators.models import Collaborator 
from apps.points.models import Point

def check_password_in_signup(password: str, confirm_password: str):
    
    if not password:
        return False

    if not confirm_password:
        return False

    if not password == confirm_password:
        return False

    return True

def get_collaborator_by_rf(rf: str):
    try:
        # Fetch collaborator by rf
        return Collaborator.objects.get(rf=rf)

    except DoesNotExist:
        return resp_does_not_exist('CollaboratorServices', 'Colaborador')

    except FieldDoesNotExist as e:
        return resp_exception('ColaboratorServices', description=e.__str__())

    except Exception as e:
        return resp_exception('ColaboratorServices', description=e.__str__())

def get_point_by_id(point_id: int):
    try:
        # Fetch point by rf
        return Point.objects.get(id=point_id)

    except DoesNotExist:
        return resp_does_not_exist('PointServices', 'ponto')

    except FieldDoesNotExist as e:
        return resp_exception('PointServices', description=e.__str__())

    except Exception as e:
        return resp_exception('PointServices', description=e.__str__())
