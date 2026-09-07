import requests
import json
import jsonpath

# Creating a new resource

# API URL
url = "https://reqres.in/api/users/2"

# Request Header Mandatory API-Key
header = {
    "x-api-key": "reqres_def4b0a2073e4578baaf0461a53840e3"
    }

# Read input json file
file = open('/home/qamaster/Projects/APIAutomation/updateUserBody.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
#print(request_json)

# Make PUT Request with Json input body
response = requests.put(url, request_json, headers = header)
print(response.status_code)
#print(response.headers)
#print(response.content)

# Validation of status code
assert response.status_code == 200

# Fetching Header from the response
print(response.headers.get('Date'))

#Parsing response to JSON format:
response_json = json.loads(response.text)
#print(response_json)

# Picking updating date
updated_date = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_date[0])