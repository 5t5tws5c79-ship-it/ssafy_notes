# 05. 자료구조 심화 — 중첩 리스트 / 딕셔너리 다루기

`jsonplaceholder.typicode.com` 응답처럼 **dict 안에 dict, 리스트 안에 dict** 로
여러 겹 중첩된 실제 API 데이터를 파고들어 원하는 형태로 정제 · 집계하는 연습.

## 구성

| 파일 | 주제 | 핵심 |
|---|---|---|
| `01_user_report.py` | 유저 데이터 정제 | 중첩 dict 파고들기 → 평탄화 → 필터 → 그룹핑 |
| `02_post_stats.py` | 게시글/댓글 집계 | 세 리스트를 id 로 join, 조회용 dict, 다중 기준 정렬 |
| `03_comment_tree.py` | 대댓글 트리 | **깊이를 모르는 중첩 구조 → 재귀** (`04_재귀함수` 와 이어짐) |

- `students/` — 문제. 함수 본문을 직접 채운다.
- `answers/` — 풀이. 주석에 왜 그렇게 되는지 적어 두었다.

## 실행

```bash
python students/01_user_report.py
python answers/01_user_report-solution.py
```

**각 파일은 완전히 자립적이다.** 데이터가 파일 맨 위에 변수로 박혀 있어서
import 도, 인터넷도, 다른 파일도 필요 없다. 파일 하나만 열면 데이터와 문제가 같이 보인다.

각 파일 하단의 주석에 정답 출력이 적혀 있으니 비교하면서 풀면 된다.

## 각 파일에 들어 있는 데이터

| 파일 | 변수 | 내용 |
|---|---|---|
| `01_user_report.py` | `USERS` | 사용자 10명. `address.geo.lat` 처럼 3단계까지 중첩 (위/경도는 **문자열**) |
| `02_post_stats.py` | `USERS` / `POSTS` / `COMMENTS` | id 로 서로 연결된 세 리스트 (사용자 10, 게시글 15, 댓글 45) |
| `03_comment_tree.py` | `THREAD` | 대댓글 트리. `replies` 안에 같은 모양이 반복되며 최대 5단까지 중첩 |

실제 API 에서 직접 받아오고 싶다면:

```python
import requests
USERS = requests.get('https://jsonplaceholder.typicode.com/users').json()
```
