"""
04. 투표 집계

> 투표용지가 이름 리스트로 주어진다. 표를 집계하는 세 함수를 작성하시오.
>
>     votes = ['kim', 'lee', 'kim', 'park', 'lee', 'kim']

---

1) count_votes(votes)
   {이름: 득표수} 를 반환한다. 표가 없으면 빈 dict.

       count_votes(['kim', 'lee', 'kim'])  #=> {'kim': 2, 'lee': 1}

2) winner(votes)
   최다 득표자 한 명을 반환한다. 동점이면 이름이 앞서는 사람이 이긴다.
   표가 하나도 없으면 빈 문자열 '' 을 반환한다.

       winner(['kim', 'ahn', 'kim', 'ahn', 'lee'])  #=> 'ahn'   (2표 동점 -> 'ahn' < 'kim')

3) ranking(votes)
   (이름, 득표수) 짝의 리스트를 득표수 내림차순으로 반환한다. 동점이면 이름 오름차순.

       ranking(['kim', 'lee', 'kim'])  #=> [('kim', 2), ('lee', 1)]

   힌트) dict 의 .items() 는 (키, 값) 짝을 꺼내 준다.
         정렬 기준이 두 개일 때는 key 에 튜플을 넘긴다. 숫자 앞에 - 를 붙이면
         그 항목만 내림차순이 된다.

             sorted(counter.items(), key=lambda item: (-item[1], item[0]))
                                                        ^득표수     ^이름
"""
from collections import defaultdict


def count_votes(votes):
    counter = defaultdict(int)

    for name in votes:
        pass

    return dict(counter)


def winner(votes):
    counter = count_votes(votes)

    best_name = ''
    best_count = 0

    for name in counter:
        # 표가 더 많거나 / 동점인데 이름이 더 앞서면 교체
        pass

    return best_name


def ranking(votes):
    counter = count_votes(votes)

    # sorted 에 key 를 넘겨 한 번에 정렬한다.
    pass


if __name__ == '__main__':
    ballots = ['kim', 'lee', 'kim', 'park', 'lee', 'kim']

    print(count_votes(ballots))   # {'kim': 3, 'lee': 2, 'park': 1}
    print(winner(ballots))        # kim
    print(ranking(ballots))       # [('kim', 3), ('lee', 2), ('park', 1)]

    # 동점 상황
    tie = ['kim', 'ahn', 'kim', 'ahn', 'lee']
    print(count_votes(tie))       # {'kim': 2, 'ahn': 2, 'lee': 1}
    print(winner(tie))            # ahn
    print(ranking(tie))           # [('ahn', 2), ('kim', 2), ('lee', 1)]

    print(count_votes([]))        # {}
    print(repr(winner([])))       # ''
