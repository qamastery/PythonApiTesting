import requests
import jsonpath
import json

def test_add_new_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("/home/qamaster/Projects/APIAutomation/dataFiles/postStudentsDetails.json",'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_update_student_data_by_id():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10891157"
    file = open("/home/qamaster/Projects/APIAutomation/dataFiles/putStudentsDetails.json",'r')
    json_request = json.loads(file.read())
    response = requests.put(API_URL,json_request)
    print(response.text)

def test_delete_student_data_by_id():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10891153"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_data_by_id():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/10891153"
    response = requests.get(API_URL)
    #json_response = json.loads(response.text) OR
    json_response = response.json()
    print(response.text)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 10891153

