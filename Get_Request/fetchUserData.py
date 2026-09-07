import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
header = {
    "x-api-key": "reqres_def4b0a2073e4578baaf0461a53840e3"
    }

response = requests.get(url, headers=header)

# 75th Session
print(response.status_code)
assert response.status_code == 200

# 76th Session
#print(response.headers)
#print(response.content)
# print(response.headers.get("Date"))
# print(response.headers.get("Server"))
# print(response.cookies)
# print(response.encoding)
# print(response.elapsed)

# 77th Session - Parse response to Json Format
json_response = json.loads(response.text)
print(json_response)

# Fetch Value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
assert pages[0] == 2