import requests

url = 'https://httpbin.org/get'

params = {"name":"parameter_first","email":"parameter_second","age":"parameter_third"}

response = requests.get(url, params=params)

print(response.status_code)
print(response.text)