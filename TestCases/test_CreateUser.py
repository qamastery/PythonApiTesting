import requests
import json
import jsonpath
import pytest

# API URL
url = "https://reqres.in/api/users"

# Request Header Mandatory API-Key
header = {
    "x-api-key": "reqres_def4b0a2073e4578baaf0461a53840e3"
    }
@pytest.fixture(scope="module")
def open_file():
    global file
    file = open('/home/qamaster/Projects/APIAutomation/createUserBody.json', 'r')

def test_create_new_user(open_file):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json, headers = header)
    assert response.status_code == 201

def test_create_another_user(open_file):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json, headers = header)
    response_json = json.loads(response.text)
    response_id = jsonpath.jsonpath(response_json, 'id')
    print(response_id[0])
    created_date = jsonpath.jsonpath(response_json, 'createdAt')
    print(created_date[0])