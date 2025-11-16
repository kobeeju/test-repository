import requests
from random import randint

BASE_URL = "http://www.randomnumberapi.com"
url = f"{BASE_URL}/api/v1.0/random"

# API로 대체
# def generate_random_number(start, end, count):
#     numbers = []
#     for _ in range(count):
#         numbers.append(randint(start, end))

#     return numbers


if __name__ == "__main__":
    print("숫자의 범위를 지정해 주세요.")
    start = int(input("시작: "))
    end = int(input("끝: "))

    params = {"min": start, "max": end, "count": 3}

    try:
        res = requests.get(url, params=params)
        data = res.json()

        print(data)
    except Exception as e:
        print(e)
    from random import randint
