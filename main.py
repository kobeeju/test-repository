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
