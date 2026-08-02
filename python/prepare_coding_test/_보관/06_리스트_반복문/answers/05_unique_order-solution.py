"""
05. 순서를 지키는 중복 제거 / 교집합 - 풀이
"""


def unique(numbers):
    result = []

    for n in numbers:
        # 아직 담지 않은 값만 담는다. -> 처음 나온 순서가 그대로 유지된다.
        if n not in result:
            result.append(n)

    return result


def common(a, b):
    result = []

    for n in a:
        # b 에도 있고, 아직 담지 않았다면 담는다.
        if n in b and n not in result:
            result.append(n)

    return result


def only_in_a(a, b):
    result = []

    for n in a:
        if n not in b and n not in result:
            result.append(n)

    return result


if __name__ == '__main__':
    print(unique([3, 1, 3, 2, 1, 5]))
    print(unique(['a', 'b', 'a']))
    print(unique([]))

    print(common([3, 1, 4, 1, 5], [1, 5, 9, 1]))
    print(common([1, 2], [3, 4]))

    print(only_in_a([3, 1, 4, 1, 5], [1, 5, 9]))

    # 참고) set 을 쓰면 한 줄이지만 순서가 보장되지 않는다.
    print(set([3, 1, 4, 1, 5]) & set([1, 5, 9]))

    # 순서까지 지키면서 짧게 쓰고 싶다면 dict 의 키가 중복을 허용하지 않는 성질을 이용한다.
    # (파이썬 3.7 부터 dict 는 넣은 순서를 기억한다)
    print(list(dict.fromkeys([3, 1, 3, 2, 1, 5])))
