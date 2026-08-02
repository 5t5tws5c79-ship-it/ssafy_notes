"""
02. 마라톤 미완주자 - 풀이
"""
from collections import defaultdict


def not_finished(participants, completions):
    # 완주자를 먼저 세어 둔다. {'kim': 2, 'park': 1, ...}
    counter = defaultdict(int)
    for name in completions:
        counter[name] += 1

    for name in participants:
        # 완주 명단에 남은 몫이 있으면 한 명 지우고 넘어간다.
        if counter[name] > 0:
            counter[name] -= 1
        # 남은 몫이 없다 = 이 사람이 못 들어왔다.
        else:
            return name

    return None


if __name__ == '__main__':
    print(not_finished(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
    print(not_finished(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
                       ['josipa', 'filipa', 'marina', 'nikola']))
    print(not_finished(['mislav', 'stanko', 'mislav', 'ana'],
                       ['stanko', 'ana', 'mislav']))

    # 아래는 흔히 하는 잘못된 풀이다. 동명이인이 있으면 틀린다.
    def wrong(participants, completions):
        for name in participants:
            if name not in completions:
                return name
        return None

    # 'mislav' 두 명 중 한 명만 완주했는데, in 검사는 "한 명이라도 있으면 True" 라서
    # 두 번째 mislav 도 완주한 것으로 보고 None 을 돌려준다.
    print(wrong(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))
