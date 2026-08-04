# 06. 반복문으로 리스트 훑기

for 문으로 리스트/문자열을 한 번 훑으면서 **세고, 거르고, 다시 이어 붙이는** 기본 패턴 연습.
코딩테스트 1번 문제 난도.

## 구성

| 파일 | 주제 | 핵심 패턴 |
|---|---|---|
| `01_count_chars.py` | 문자 개수 세기 | `defaultdict(int)` 로 카운팅, dict 순회하며 최댓값 찾기 |
| `02_marathon.py` | 마라톤 미완주자 | **동명이인 함정** — `in` 으로 풀면 틀린다 |
| `03_number_string.py` | 숫자 문자열 다루기 | `split()` → `map(int, …)` → 처리 → `join()` |
| `04_vote.py` | 투표 집계 | 카운팅 + 동점 처리 + `sorted(key=lambda …)` 다중 기준 정렬 |
| `05_unique_order.py` | 순서 지키는 중복 제거 | `set` 없이 "결과에 없으면 담는다" 패턴 |

- `students/` — 문제. 함수 본문을 직접 채운다.
- `answers/` — 풀이. 흔한 오답과 표준 라이브러리 대안도 함께 적어 두었다.

## 실행

```bash
python students/01_count_chars.py
python answers/01_count_chars-solution.py
```

각 파일 하단에 정답 출력이 주석으로 달려 있으니 비교하며 풀면 된다.
지금 그대로 실행하면 빈 값이나 `None` 이 나온다 — 아직 안 채웠기 때문이다.

## 반복되는 핵심 패턴 3가지

```python
# 1. 세기 — if 로 키 존재 확인할 필요가 없다
from collections import defaultdict
counter = defaultdict(int)
for item in items:
    counter[item] += 1

# 2. 거르기 — 결과 리스트를 만들어 조건에 맞는 것만 담는다
result = []
for item in items:
    if 조건:
        result.append(item)

# 3. 두 기준으로 정렬 — 숫자 앞의 - 가 그 항목만 내림차순으로 만든다
sorted(counter.items(), key=lambda item: (-item[1], item[0]))
```
