"""
01. 문자 개수 세기

> 문자열을 한 글자씩 돌면서, 각 글자가 몇 번 나왔는지 세는 연습.
> dict 는 for 문으로 돌리면 '키'가 하나씩 나온다는 점을 기억할 것.

---

1) count_chars(word)
   각 글자가 등장한 횟수를 {글자: 횟수} 형태로 반환한다.

       count_chars('banana')  #=> {'b': 1, 'a': 3, 'n': 2}

   힌트) defaultdict(int) 를 쓰면 "이 키가 이미 있나?" 를 if 로 확인하지 않아도
         조회하는 순간 0 으로 초기화된다.

           from collections import defaultdict
           counter = defaultdict(int)
           counter['a'] += 1     # 'a' 가 없어도 에러 없이 1 이 된다

2) most_common(word)
   가장 많이 등장한 글자 하나를 반환한다.
   횟수가 같다면 알파벳 순서가 앞서는 글자를 고를 것. (문자열끼리도 < 로 비교된다)

       most_common('banana')  #=> 'a'
       most_common('aabb')    #=> 'a'   (2번씩 동점 -> 앞서는 'a')
"""
from collections import defaultdict


def count_chars(word):
    counter = defaultdict(int)

    # 문자열을 for 로 돌리면 한 글자씩 나온다.
    for char in word:
        pass

    # 비교하기 편하도록 일반 dict 로 바꿔서 반환한다.
    return dict(counter)


def most_common(word):
    counter = count_chars(word)

    # 가장 많이 나온 글자와 그 횟수를 담아둘 변수를 먼저 만들어 두고,
    # dict 를 순회하면서 더 나은 후보를 만나면 교체한다.
    best_char = ''
    best_count = 0

    for char in counter:
        pass

    return best_char


if __name__ == '__main__':
    print(count_chars('banana'))   # {'b': 1, 'a': 3, 'n': 2}
    print(count_chars('ssafy'))    # {'s': 2, 'a': 1, 'f': 1, 'y': 1}
    print(count_chars(''))         # {}

    print(most_common('banana'))   # a
    print(most_common('ssafy'))    # s
    print(most_common('aabb'))     # a
