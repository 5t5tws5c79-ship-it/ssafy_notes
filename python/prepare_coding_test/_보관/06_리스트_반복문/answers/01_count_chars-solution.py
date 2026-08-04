"""
01. 문자 개수 세기 - 풀이
"""
from collections import defaultdict


def count_chars(word):
    # 조회 즉시 0 으로 초기화되므로 "키가 있나?" 를 if 로 확인할 필요가 없다.
    counter = defaultdict(int)

    for char in word:
        counter[char] += 1

    # 채점/비교를 편하게 하려고 일반 dict 로 바꿔 반환한다.
    return dict(counter)


def most_common(word):
    counter = count_chars(word)

    best_char = ''
    best_count = 0

    for char in counter:
        # 더 많이 나왔거나, 같은 횟수인데 알파벳이 더 앞서면 교체
        if counter[char] > best_count or (counter[char] == best_count and char < best_char):
            best_char = char
            best_count = counter[char]

    return best_char


if __name__ == '__main__':
    print(count_chars('banana'))
    print(count_chars('ssafy'))
    print(count_chars(''))

    print(most_common('banana'))
    print(most_common('ssafy'))
    print(most_common('aabb'))

    # 참고) 표준 라이브러리에는 이 일을 하는 Counter 가 이미 있다.
    from collections import Counter
    print(Counter('banana'))
    print(Counter('banana').most_common(1))
