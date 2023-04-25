# # 10952번 : while문으로 반복하기
# 두 정수 A와 B를 입력받은 다음, A+B를 출력

#  입력은 여러 개의 테스트 케이스
while True:
    A, B = map(int, input().split())  # 각 줄에 A와 B
    a_b = A + B  # A + B를 더한값을 변수 a_b에 할당
    if a_b == 0:  # A+B가 0이면 멈추고
        break
    else:
        print(a_b)  # 아니면 A+B 출력
