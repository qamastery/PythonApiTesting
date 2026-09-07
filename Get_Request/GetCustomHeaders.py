import requests

url = 'https://httpbin.org/get?'

custom_header = {"A1":"QAMASTER","A2":"THEBEST"}

response = requests.get(url, headers=custom_header)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)