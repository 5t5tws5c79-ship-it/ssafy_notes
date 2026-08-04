"""
08. 십진수를 이진수 문자열로

> 0 이상의 정수 n을 입력받아 2진수 표현을 문자열로 반환하는 함수를 재귀로 작성하시오.
> (내장 함수 bin() 은 사용하지 않는다.)
>
> 힌트) 13을 2로 나누면 몫 6, 나머지 1
>       -> to_binary(13) = to_binary(6) + '1'

예시)
    to_binary(0)   #=> '0'
    to_binary(5)   #=> '101'
    to_binary(13)  #=> '1101'
"""


def to_binary(n):
    # 종료 조건: n이 0 또는 1이면 그대로 문자열로 반환합니다.

    # 재귀 호출: (n // 2 의 이진수) + (n % 2 를 문자열로)
    pass


if __name__ == '__main__':
    print(to_binary(0))    # '0'
    print(to_binary(1))    # '1'
    print(to_binary(5))    # '101'
    print(to_binary(13))   # '1101'
    print(to_binary(255))  # '11111111'
