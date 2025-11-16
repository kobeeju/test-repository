import requests

BASE_URL = "http://www.randomnumberapi.com"
url = f"{BASE_URL}/api/v1.0/random"

params = {
    'min': 0,
    'max': 9,
    'count': 3
}

try:
    res = requests.get(url, params=params)
    data = res.json()

    print(data)
except Exception as e:
    print(e)
