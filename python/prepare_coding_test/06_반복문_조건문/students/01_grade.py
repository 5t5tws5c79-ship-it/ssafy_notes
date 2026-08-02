"""
01. 성적 등급 매기기

> if / elif / else 연습.
>
> ⚠️ 조건문은 위에서부터 순서대로 검사하다가 **처음 True 를 만나는 순간 거기서 끝난다.**
>    그래서 조건을 쓰는 순서가 결과를 바꾼다. 이 문제의 핵심이다.

---

1) get_grade(score)
   점수를 받아 등급 문자열을 반환한다.

       90점 이상 -> 'A'
       80점 이상 -> 'B'
       70점 이상 -> 'C'
       60점 이상 -> 'D'
       그 외     -> 'F'

   ⚠️ '이상' 이므로 딱 90점도 A 다. (90 초과가 아니다)

2) grade_all(scores)
   점수 리스트를 받아 등급 리스트를 반환한다.
   힌트) 위에서 만든 get_grade 를 반복문 안에서 그대로 불러 쓰면 된다.

       grade_all([95, 82, 71])  #=> ['A', 'B', 'C']

3) count_pass(scores)
   60점 이상인 사람이 몇 명인지 센다.

       count_pass([95, 82, 71, 64, 30])  #=> 4
"""


def get_grade(score):
    # 어떤 조건을 맨 위에 써야 할까? 좁은 조건(높은 점수)부터 쓴다.
    pass


def grade_all(scores):
    result = []

    for score in scores:
        # get_grade 를 불러서 결과를 담는다.
        pass

    return result


def count_pass(scores):
    # 개수를 셀 변수를 0으로 만들어 두고, 조건에 맞을 때만 1씩 더한다.
    count = 0

    for score in scores:
        pass

    return count


if __name__ == '__main__':
    print(get_grade(95))    # A
    print(get_grade(90))    # A   <- 딱 90점도 A 여야 한다
    print(get_grade(89))    # B
    print(get_grade(60))    # D
    print(get_grade(59))    # F
    print(get_grade(0))     # F

    scores = [95, 82, 71, 64, 30]
    print(grade_all(scores))   # ['A', 'B', 'C', 'D', 'F']
    print(count_pass(scores))  # 4

    print(grade_all([]))       # []
    print(count_pass([]))      # 0
