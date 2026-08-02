"""
07. 거듭제곱

> 밑 base와 0 이상의 지수 exp를 입력받아 base ** exp 를 반환하는 함수를 재귀로 작성하시오.
> (** 연산자와 pow() 는 사용하지 않는다.)

예시)
    power(2, 0)   #=> 1
    power(2, 10)  #=> 1024
    power(5, 3)   #=> 125
"""


def power(base, exp):
    # 종료 조건: 어떤 수든 0제곱은 1입니다.

    # 재귀 호출: base * base^(exp-1)
    pass


if __name__ == '__main__':
    print(power(2, 0))   # 1
    print(power(2, 10))  # 1024
    print(power(5, 3))   # 125
    print(power(3, 4))   # 81
