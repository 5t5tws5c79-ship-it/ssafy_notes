"""
01. 팩토리얼 - 풀이
"""


def factorial(n):
    # 종료 조건: n이 1 이하이면 1을 반환합니다. (0! = 1, 1! = 1)
    if n <= 1:
        return 1

    # 재귀 호출: n! = n * (n-1)!
    return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(0))   # 1
    print(factorial(1))   # 1
    print(factorial(5))   # 120
    print(factorial(10))  # 3628800

    # 참고) 반복문 풀이
    def factorial_while(n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result

    print(factorial_while(5))  # 120
