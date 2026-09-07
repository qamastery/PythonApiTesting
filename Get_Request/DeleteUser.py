import requests

# API URL

url = "https://reqres.in/api/users/2"
header = {
    "x-api-key": "reqres_def4b0a2073e4578baaf0461a53840e3"
    }

response = requests.delete(url, headers=header)
print(response.status_code)
assert response.status_code == 204