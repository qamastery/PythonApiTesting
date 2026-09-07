import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
header = {
    "x-api-key": "reqres_def4b0a2073e4578baaf0461a53840e3"
    }

response = requests.get(url, headers=header)
#print(response.text)
json_response = json.loads(response.text)

for i in range (0,6):
    first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name[0])
