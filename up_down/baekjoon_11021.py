# 11021번 : A+B - 7
# 두 정수 A와 B를 입력받은 다음, A+B를 출력

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
T = int(input())

for i in range(1, T + 1):  # 1부터 T까지
    # 각 테스트 케이스는 한 줄로,각 줄에 A와 B가 주어진다.
    A, B = map(int, input().split())
    case = A + B
    # 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력
    print("Case #" + str(i) + ":", case)  # str로 문자열 변환
