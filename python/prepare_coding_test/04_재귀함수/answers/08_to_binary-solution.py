"""
08. 십진수를 이진수 문자열로 - 풀이
"""


def to_binary(n):
    # 종료 조건: 0 또는 1은 그대로 문자열로 반환합니다.
    if n < 2:
        return str(n)

    # 재귀 호출: 몫의 이진수 뒤에 나머지를 붙입니다.
    return to_binary(n // 2) + str(n % 2)


if __name__ == '__main__':
    print(to_binary(0))    # '0'
    print(to_binary(1))    # '1'
    print(to_binary(5))    # '101'
    print(to_binary(13))   # '1101'
    print(to_binary(255))  # '11111111'

    # 동작 과정
    # to_binary(13)
    #   -> to_binary(6) + '1'
    #        -> to_binary(3) + '0'
    #             -> to_binary(1) + '1'
    #                  -> '1'        (종료 조건 도달)
    #             -> '1' + '1'  = '11'
    #        -> '11' + '0' = '110'
    #   -> '110' + '1' = '1101'

    # 내장 함수와 비교 (bin()은 앞에 '0b'가 붙습니다)
    print(bin(13))  # '0b1101'
