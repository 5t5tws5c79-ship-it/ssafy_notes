"""
07. 거듭제곱 - 풀이
"""


def power(base, exp):
    # 종료 조건: 어떤 수든 0제곱은 1입니다.
    if exp == 0:
        return 1

    # 재귀 호출: base^exp = base * base^(exp-1)
    return base * power(base, exp - 1)


if __name__ == '__main__':
    print(power(2, 0))   # 1
    print(power(2, 10))  # 1024
    print(power(5, 3))   # 125
    print(power(3, 4))   # 81

    # 참고) 분할 정복으로 호출 횟수를 크게 줄일 수 있습니다.
    #       exp가 짝수면 base^exp = (base^(exp//2))^2 이므로 절반씩 줄어듭니다.
    def fast_power(base, exp):
        if exp == 0:
            return 1
        half = fast_power(base, exp // 2)
        if exp % 2 == 0:
            return half * half
        return half * half * base

    print(fast_power(2, 10))  # 1024
