"""
03. 조건에 맞는 것만 골라내기 - 풀이
"""


def evens(numbers):
    result = []

    for n in numbers:
        # 2로 나눈 나머지가 0이면 짝수
        if n % 2 == 0:
            result.append(n)

    return result


def between(numbers, low, high):
    result = []

    for n in numbers:
        # low '이상' high '이하' 이므로 등호가 붙는다.
        # 파이썬은 low <= n <= high 처럼 이어서 쓸 수 있다.
        if low <= n <= high:
            result.append(n)

    return result


def count_sign(numbers):
    positive = 0
    negative = 0
    zero = 0

    for n in numbers:
        # 카운터 여러 개를 동시에 세는 전형적인 패턴
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1

    return positive, negative, zero


if __name__ == '__main__':
    print(evens([1, 2, 3, 4, 5, 6]))   # [2, 4, 6]
    print(evens([1, 3, 5]))            # []
    print(evens([0, -2, -3]))          # [0, -2]

    print(between([1, 5, 10, 15, 20], 5, 15))   # [5, 10, 15]
    print(between([1, 5, 10], 100, 200))        # []

    print(count_sign([1, -2, 0, 5, -7, 0]))   # (2, 2, 2)
    print(count_sign([]))                     # (0, 0, 0)

    # 반환값이 3개처럼 보이지만 실제로는 튜플 하나다. 언패킹해서 받을 수 있다.
    p, n, z = count_sign([1, -2, 0])
    print(f'양수 {p}개, 음수 {n}개, 0 은 {z}개')   # 양수 1개, 음수 1개, 0 은 1개

    # ------------------------------------------------------------------
    # 흔한 오답 1) '초과/미만' 과 '이상/이하' 를 헷갈림
    def wrong_between(numbers, low, high):
        result = []
        for n in numbers:
            if low < n < high:      # 등호가 빠져서 경계값이 빠진다
                result.append(n)
        return result

    print(wrong_between([1, 5, 10, 15, 20], 5, 15))   # [10]  <- 5와 15가 사라짐

    # 흔한 오답 2) elif 대신 if 를 세 번 쓰면? 이 경우엔 결과가 같다.
    #             조건들이 서로 겹치지 않기 때문. 하지만 겹치는 조건이라면
    #             if 3개는 여러 개가 동시에 실행되므로 결과가 달라진다.
