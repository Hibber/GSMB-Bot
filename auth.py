import requests


def get_token(x):
    url = "https://us.battle.net/oauth/token"
    payload = 'grant_type=client_credentials'
    headers = {
        'Authorization': 'Basic '
                         'ZmMzZWM3OGFjZGI1NGU5MmJiZjhkNzU0YjVlYTk3NTI6VTU4VGVuS2hUYTVTbnJlUW1MZlF2WDhnUUw3dFk5QzM=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    data = x.response(response['access_token'])
    return data['access_token']


