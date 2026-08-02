"""
02. 1부터 n까지의 합 - 풀이
"""


def sum_to_n(n):
    # 종료 조건: 더할 수가 1 하나만 남으면 1을 반환합니다.
    if n <= 1:
        return n

    # 재귀 호출: n + (1부터 n-1까지의 합)
    return n + sum_to_n(n - 1)


if __name__ == '__main__':
    print(sum_to_n(1))    # 1
    print(sum_to_n(5))    # 15
    print(sum_to_n(10))   # 55
    print(sum_to_n(100))  # 5050

    # 콜 스택 확인
    # sum_to_n(4)
    #   -> 4 + sum_to_n(3)
    #        -> 3 + sum_to_n(2)
    #             -> 2 + sum_to_n(1)
    #                  -> 1          (종료 조건 도달)
    #             -> 2 + 1 = 3
    #        -> 3 + 3 = 6
    #   -> 4 + 6 = 10
