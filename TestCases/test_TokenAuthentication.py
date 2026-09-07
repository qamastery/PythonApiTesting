import requests

def test_token_auth():
    access_token = "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"
    api_url = "https://api.github.com/user"
    headers = {"Authorization": f"Bearer {access_token}",
               "X-GitHub-Api-Version": "2026-03-10"
               }
    response = requests.get(api_url,headers=headers)
    print(response.text)

