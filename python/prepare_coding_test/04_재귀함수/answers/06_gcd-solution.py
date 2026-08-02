"""
06. 최대공약수 (유클리드 호제법) - 풀이
"""


def gcd(a, b):
    # 종료 조건: b가 0이면 a가 최대공약수입니다.
    if b == 0:
        return a

    # 재귀 호출: gcd(a, b) = gcd(b, a % b)
    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(12, 18))   # 6
    print(gcd(48, 18))   # 6
    print(gcd(17, 5))    # 1
    print(gcd(100, 75))  # 25

    # 동작 과정
    # gcd(48, 18) -> gcd(18, 12) -> gcd(12, 6) -> gcd(6, 0) -> 6

    # 참고) 최소공배수는 두 수의 곱을 최대공약수로 나누면 됩니다.
    def lcm(a, b):
        return a * b // gcd(a, b)

    print(lcm(4, 6))  # 12
