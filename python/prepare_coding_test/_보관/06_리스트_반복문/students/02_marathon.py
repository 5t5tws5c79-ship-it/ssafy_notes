"""
02. 마라톤 미완주자

> 마라톤에 참여한 선수 이름 리스트 participants 와
> 완주한 선수 이름 리스트 completions 가 주어진다.
> 완주하지 못한 선수는 딱 한 명이다. 그 선수의 이름을 반환하는 함수를 작성하시오.

       not_finished(['leo', 'kiki', 'eden'], ['eden', 'kiki'])   #=> 'leo'

---

⚠️ 함정: 참가자 중에 **동명이인이 있을 수 있다.**

       participants = ['mislav', 'stanko', 'mislav', 'ana']
       completions  = ['stanko', 'ana', 'mislav']
       #=> 'mislav'   (mislav 두 명 중 한 명만 완주)

   아래처럼 `in` 으로만 검사하면 이 경우에 틀린다.
   `in` 은 "한 명이라도 있으면 True" 라서 두 번째 mislav 도 완주한 것으로 보기 때문이다.

       for name in participants:
           if name not in completions:   # <- 동명이인이 있으면 통과해 버림
               return name

   힌트) 이름을 세어 두고, 한 명씩 지워 나가면 된다.
         완주자를 {이름: 완주한 인원수} 로 만든 뒤 참가자를 돌면서
         남은 몫이 있으면 1 빼고, 남은 몫이 없으면 그 사람이 정답이다.
"""
from collections import defaultdict


def not_finished(participants, completions):
    # 1) 완주자 수를 센다. {'mislav': 1, 'stanko': 1, 'ana': 1}
    counter = defaultdict(int)
    for name in completions:
        pass

    # 2) 참가자를 돌면서 완주 명단에서 한 명씩 지운다.
    for name in participants:
        # 남은 몫이 있으면 -> 1 빼고 넘어간다
        # 남은 몫이 없으면 -> 이 사람이 미완주자
        pass

    return None


if __name__ == '__main__':
    print(not_finished(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
    # leo

    print(not_finished(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
                       ['josipa', 'filipa', 'marina', 'nikola']))
    # vinko

    print(not_finished(['mislav', 'stanko', 'mislav', 'ana'],
                       ['stanko', 'ana', 'mislav']))
    # mislav   <- 이게 나와야 통과. None 이 나오면 위 함정에 걸린 것이다.
