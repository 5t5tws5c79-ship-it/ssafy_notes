"""
01. 성적 등급 매기기 - 풀이
"""


def get_grade(score):
    # 좁은 조건(높은 점수)부터 위에 둔다.
    # 위에서부터 순서대로 검사하다가 처음 True 를 만나면 거기서 끝나기 때문이다.
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def grade_all(scores):
    result = []

    for score in scores:
        result.append(get_grade(score))

    return result


def count_pass(scores):
    count = 0

    for score in scores:
        if score >= 60:
            count += 1

    return count


if __name__ == '__main__':
    print(get_grade(95))    # A
    print(get_grade(90))    # A  (90 '이상' 이므로 딱 90도 A)
    print(get_grade(89))    # B
    print(get_grade(60))    # D
    print(get_grade(59))    # F
    print(get_grade(0))     # F

    scores = [95, 82, 71, 64, 30]
    print(grade_all(scores))   # ['A', 'B', 'C', 'D', 'F']
    print(count_pass(scores))  # 4

    print(grade_all([]))       # []
    print(count_pass([]))      # 0

    # ------------------------------------------------------------------
    # 흔한 오답: 조건 순서를 뒤집으면 전부 같은 등급이 나온다.
    def wrong_grade(score):
        if score >= 60:      # 95도 60 이상이라 여기서 걸려버린다
            return 'D'
        elif score >= 70:    # 여기까지 오지도 못함
            return 'C'
        elif score >= 80:
            return 'B'
        elif score >= 90:
            return 'A'
        else:
            return 'F'

    print([wrong_grade(s) for s in scores])   # ['D', 'D', 'D', 'D', 'F']
