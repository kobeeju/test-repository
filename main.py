import requests

url = ""

try:
    res = requests.get(url)
    data = res.json()

    print(data)
except Exception as e:
    print(e)
