from mongoengine.errors import FieldDoesNotExist, DoesNotExist

from apps.responses import resp_exception, resp_does_not_exist

from apps.collaborators.models import Collaborator 


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
        # buscamos todos os usuários da base utilizando o paginate
        return Collaborator.objects.get(rf=rf)

    except DoesNotExist:
        return resp_does_not_exist('CollaboratorServices', 'Colaborador')

    except FieldDoesNotExist as e:
        return resp_exception('ColaboratorServices', description=e.__str__())

    except Exception as e:
        return resp_exception('ColaboratorServices', description=e.__str__())
