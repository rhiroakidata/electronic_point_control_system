import requests, json

from apps.messages import (
    MSG_ALREADY_EXISTS
)

def test_post_collaborator():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    new_collaborator = {
        "name": "Nome teste",
        "email": "emailteste@gmail.com",
        "password": "123456",
        "confirm_password": "123456"
    }
    
    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(new_collaborator)
    )
    response_json = response.json()
    status = response.status_code
    new_collaborator_response = response_json['data']
    
    assert status == 200 and new_collaborator_response['id'] is not None

def test_get_list_collaborators():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    status = response_json['status']
    list_size = len(response_json['data'])
    
    assert status == 200 and list_size > 0
    
def test_get_collaborator():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    rf = response_json['data'][0]['rf']
    
    url = 'http://0.0.0.0:5000/collaborators/' + str(rf)
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    status = response_json['status']
    rf_response = response_json['data']['rf']
    
    assert status == 200 and rf==rf_response

def test_delete_collaborator():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    rf = response_json['data'][0]['rf']
    
    url = 'http://0.0.0.0:5000/collaborators/' + str(rf)
    
    response = requests.delete(url)
    
    assert response.status_code == 200
    
def test_invalid_post():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    new_collaborator = {
        "name": "",
        "email": "",
        "password": "",
        "confirm_password": ""
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(new_collaborator)
    )
    response_json = response.json()
    status = response.status_code
    
    assert status == 422
    
def test_unmatch_password():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    new_collaborator = {
        "name": "Nome teste",
        "email": "emailteste@gmail.com",
        "password": "654321",
        "confirm_password": "123456"
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(new_collaborator)
    )
    response_json = response.json()
    status = response.status_code
    
    assert status == 422

def test_already_exists():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    new_collaborator = {
        "name": "Teste",
        "email": "testeemail@gmail.com",
        "password": "123456",
        "confirm_password": "123456"
    }
    
    url = 'http://0.0.0.0:5000/collaborators'
    
    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(new_collaborator)
    )
    
    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(new_collaborator)
    )
    response_json = response.json()
    status = response.status_code
    message = response_json['message']
    
    assert (status == 400 
            and message==MSG_ALREADY_EXISTS.format('colaborador'))   
