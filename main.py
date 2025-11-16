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
from random import randint


def generate_random_number(start, end, count):
    numbers = []
    for _ in range(count):
        numbers.append(randint(start, end))

    return numbers


if __name__ == "__main__":
    print("숫자의 범위를 지정해 주세요.")
    start = int(input("시작: "))
    end = int(input("끝: "))
    
    print(generate_random_number(start, end, count=3))
