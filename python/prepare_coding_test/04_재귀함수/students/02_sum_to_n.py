"""
02. 1부터 n까지의 합

> 자연수 n을 입력받아 1 + 2 + 3 + ... + n 의 결과를 반환하는 함수를 재귀로 작성하시오.

예시)
    sum_to_n(1)   #=> 1
    sum_to_n(5)   #=> 15
    sum_to_n(100) #=> 5050
"""


def sum_to_n(n):
    # 종료 조건: 더할 수가 하나 남았을 때(n이 1일 때)

    # 재귀 호출: n + (1부터 n-1까지의 합)
    pass


if __name__ == '__main__':
    print(sum_to_n(1))    # 1
    print(sum_to_n(5))    # 15
    print(sum_to_n(10))   # 55
    print(sum_to_n(100))  # 5050
