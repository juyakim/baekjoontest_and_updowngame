import random

# updown 게임

# 조건문을 추가해서 사용자 인풋이 정답보다 작다면 up
# 정답보다 크다면 down을 프린트하게 해주세요
answer = random.randint(1, 10)
while True:
    user_input = int(input("1 ~ 10 사이의 숫자를 입력하세요: "))
    if user_input < answer:
        print("UP")
    elif user_input > answer:
        print("DOWN")
    elif user_input == answer:
        print(f"정답 {answer} 입니다!")
        break
