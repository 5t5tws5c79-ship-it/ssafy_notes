"""
01. 팩토리얼

> n! = n x (n-1) x (n-2) x ... x 1
>
> 자연수 n을 입력받아 n의 팩토리얼을 반환하는 함수를 재귀로 작성하시오.
> (단, 0! 은 1이다.)

예시)
    factorial(0)  #=> 1
    factorial(5)  #=> 120
    factorial(10) #=> 3628800
"""


def factorial(n):
    # 종료 조건: n이 1 이하이면 1을 반환합니다.

    # 재귀 호출: n * (n-1)! 형태로 문제를 작게 만듭니다.
    pass


if __name__ == '__main__':
    print(factorial(0))   # 1
    print(factorial(1))   # 1
    print(factorial(5))   # 120
    print(factorial(10))  # 3628800
