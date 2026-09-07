import requests
import json
import jsonpath

def test_add_new_data():
    app_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("/home/qamaster/Projects/APIAutomation/dataFiles/postStudentsDetails.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(app_url,request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    skills_url ="https://thetestingworldapi.com/api/technicalskills"
    file = open("/home/qamaster/Projects/APIAutomation/dataFiles/postSkills.json", 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(skills_url, request_json)
    print(response.text)

    addr_url ="https://thetestingworldapi.com/api/addresses"
    file = open("/home/qamaster/Projects/APIAutomation/dataFiles/postAddress.json", 'r')
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response = requests.post(addr_url, request_json)
    print(response.text)

    final_data_url = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_data_url, request_json)
    print(response.text)

