import requests
import json
import jsonpath

def test_oauth_api():
    token_url = "https://thetestingworldapi.com/token"
    data = {'grant_type':'password','username':'admin','password':'pa$$word'}
    response = requests.post(token_url,data)
    token_value=jsonpath.jsonpath(response.json,'access_token')

    auth= {'Authorization':'Bearer' + str(token_value[0])}
    api_url = "https://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(api_url,headers=auth)
    print(response.text)