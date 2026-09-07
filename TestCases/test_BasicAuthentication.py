import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('qamastery','8278di1g'))
    print(response.text)