import requests, json

def test_post_point():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/points'
    
    new_point = {
        "date": "2020-06-14",
        "time": "08:00:00",
        "rf": "411703"
    }
    
    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(new_point)
    )
    response_json = response.json()
    status = response.status_code
    new_point_response = response_json['data']
    
    assert status == 200 and new_point_response['id'] is not None

def test_get_list_points():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/points'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    status = response_json['status']
    list_size = len(response_json['data'])
    
    assert status == 200 and list_size > 0
    
def test_get_point():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/points'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    point_id = response_json['data'][0]['id']
    
    url = 'http://0.0.0.0:5000/points/' + str(point_id)
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    status = response_json['status']
    id_response = response_json['data']['id']
    
    assert status == 200 and point_id==id_response

def test_delete_point():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/points'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    point_id = response_json['data'][0]['id']
    print(point_id)
    
    url = 'http://0.0.0.0:5000/points/' + str(point_id)
    
    response = requests.delete(url)
    
    assert response.status_code == 200
    
def test_report():
    headers = {
        'Accept': '*/*',
        'User-agent': 'request',
    }
    
    url = 'http://0.0.0.0:5000/collaborators/411703/month/06'
    
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
    status = response_json['status']
    list_size = len(response_json['data'])
    
    assert status == 200 and list_size > 0
