import requests


def get_token(x):
    url = "https://us.battle.net/oauth/token"
    payload = 'grant_type=client_credentials'
    headers = {
        'Authorization': 'Basic '
                         '{WOW_CLIENT_ID}:{WOW_CLIENT_SECRET}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    data = x.response(response['access_token'])
    return data['access_token']


