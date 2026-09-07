import requests
import json
import jsonpath

# Creating a new resource

# API URL
url = "https://reqres.in/api/users"

# Request Header Mandatory API-Key
header = {
    "x-api-key": "reqres_def4b0a2073e4578baaf0461a53840e3"
    }

# Read input json file
file = open('/home/qamaster/Projects/APIAutomation/createUserBody.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json) # Printing input file in json format

# Make POST Request with Json input body
#response = requests.post(url, request_json, headers = header)
#print(response.status_code)
#print(response.content)

# Validation of status code
#assert response.status_code == 201

# Fetching Header from the response
#print(response.headers.get('Date'))

#Parsing response to JSON format:
#response_json = json.loads(response.text)
#print(response_json)

# Picking 'Id' using JSON Path
#response_id = jsonpath.jsonpath(response_json, 'id')
#print(response_id[0])

# Picking 'createdAt' using JSON Path
#created_date = jsonpath.jsonpath(response_json, 'createdAt')
#print(created_date[0])