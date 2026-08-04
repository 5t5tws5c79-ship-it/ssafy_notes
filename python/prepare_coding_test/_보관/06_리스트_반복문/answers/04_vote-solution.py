"""
04. 투표 집계 - 풀이
"""
from collections import defaultdict


def count_votes(votes):
    counter = defaultdict(int)

    for name in votes:
        counter[name] += 1

    return dict(counter)


def winner(votes):
    counter = count_votes(votes)

    best_name = ''
    best_count = 0

    for name in counter:
        # 표가 더 많거나, 동점인데 이름이 더 앞서면 교체
        if counter[name] > best_count or (counter[name] == best_count and name < best_name):
            best_name = name
            best_count = counter[name]

    return best_name


def ranking(votes):
    counter = count_votes(votes)

    # 표 내림차순(-), 같으면 이름 오름차순
    # counter.items() 는 (이름, 표수) 짝을 꺼내 준다.
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


if __name__ == '__main__':
    ballots = ['kim', 'lee', 'kim', 'park', 'lee', 'kim']

    print(count_votes(ballots))
    print(winner(ballots))
    print(ranking(ballots))

    # 동점 상황 (kim 2표, ahn 2표 -> 이름이 앞서는 ahn 이 이긴다)
    tie = ['kim', 'ahn', 'kim', 'ahn', 'lee']
    print(count_votes(tie))
    print(winner(tie))
    print(ranking(tie))

    print(count_votes([]))
    print(repr(winner([])))
