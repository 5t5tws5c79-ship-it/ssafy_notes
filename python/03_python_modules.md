# Python 모듈 정리 (Modules & Packages)

## 1. 모듈 (Module)

**모듈이란?** 특정한 기능을 하는 **하나의 파이썬 파일**. 변수와 함수의 모음이다.

> 과학자나 수학자는 필요한 상수나 이론을 새롭게 증명하거나 만들지 않고, **이미 검증된 상수나 이론을 사용**한다.
> 개발자도 마찬가지로, 생산성을 위해 **다른 개발자가 검증해놓은 코드를 가져다 쓴다.**

### 1.1 예시 — `math` 모듈

```python
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(4))   # 2.0
```

---

## 2. 모듈 활용 방법

### 2.1 `import` 문 + 점(`.`) 연산자

```python
import math
print(math.pi)
```

- **점(`.`) 연산자의 의미:** "왼쪽의 객체에서 `.`의 오른쪽 이름을 찾아라"
- **단점:** 매번 모듈명을 붙여야 해서 **코드가 길어질 수 있다.**

### 2.2 `from` 절 사용

필요한 것만 **콕 집어서** 가져오는 방식.

```python
from math import pi, sqrt

print(pi)        # 모듈명을 명시하지 않고 바로 사용
print(sqrt(4))
```

### 2.3 언제 뭘 쓰나? — 비교표

| 방식 | 적합한 상황 |
|------|-------------|
| `import 모듈` | 모듈 이름이 **짧고**, 어디서 온 함수인지 **출처를 드러내고 싶을 때** |
| `from 모듈 import 대상` | **반복 호출**이 잦거나, **모듈 경로가 깊어** `from` 없이는 너무 장황해질 때 |

> **정리:** 옳고 그름의 문제가 아니라 **팀 컨벤션**을 따르되, **한 파일 안에서는 통일**할 것.
> 임포트와 `from` 절을 적절히 섞어서, **남기고 싶은 출처만큼만** 남기는 게 핵심이다.

---

## 3. 이름 충돌 다루기

같은 이름을 두 번 가져오면 **나중 것이 이긴다.** (나중에 임포트한 것이 호출됨)

```python
from math import sqrt
from my_module import sqrt   # 이후 sqrt()는 my_module의 것

sqrt(4)   # my_module의 sqrt가 호출됨
```

### 3.1 `as` 키워드 — 별칭(alias) 부여

`as`로 별칭을 주면 이름 충돌을 해결하고 **둘을 공존**시킬 수 있다.

```python
from math import sqrt as math_sqrt
from my_module import sqrt as my_sqrt

math_sqrt(4)   # 2.0
my_sqrt(4)     # 내 모듈의 sqrt
```

### 3.2 ⚠️ `from module import *` 는 권장하지 않는다

- 무엇이 들어왔는지 알 수 없어 **이름 충돌**이 생기기 쉽고, 코드의 **출처 추적**이 어려워진다.

---

## 4. 사용자 정의 모듈 & 패키지

개발의 역사가 길어지면서 **코드 양이 많아져** 모듈 하나로는 감당이 안 되기 시작했다.

### 4.1 패키지 (Package)

**패키지란?** 연관된 **모듈들을 하나의 디렉토리에 모아 놓은 것**.

> 이미 누군가 잘 만들어 둔 **코드 꾸러미**다. 공구 세트가 있으면 편한 것처럼, 사용자가 모든 기능을 다 만들기는 어려우므로 잘 만들어둔 유용한 도구(모듈)들을 모아 하나로 묶은 것이 패키지다.

> **관점 정리:** 모듈과 패키지 관점에서 보면 **모든 디렉토리가 하나의 패키지**이고, **모든 파이썬 파일이 하나의 모듈**이다.

### 4.2 패키지의 사용 목적

- 모듈들의 **이름 공간(namespace)을 구분**하여 충돌을 방지
- 모듈들을 **효율적으로 관리**할 수 있도록 도움

> **설계 팁:** 너무 많은 기능이 한 파일에 몰려 있으면 사용자가 헷갈린다. **비슷한 것끼리만 묶어라.**

---

## 5. 라이브러리 (Library)

**라이브러리란?** **패키지의 묶음.**

모듈(파일) → 패키지(디렉토리) → 라이브러리(패키지 묶음)

### 5.1 파이썬 표준 라이브러리 (PSL, Python Standard Library)

파이썬 언어와 **함께 제공되는** 다양한 모듈과 패키지의 모음. 별도 설치 없이 **빌트인**되어 있다.

다양한 기능이 있어 쉽게 처리할 수 있다:

```python
math      # 수학
random    # 난수
sys       # 시스템
json      # JSON 처리
email     # 이메일
```

### 5.2 외부 패키지 (Third-party Package)

전 세계 개발자들이 만든 다양한 패키지들이 존재한다. (`pandas`, `matplotlib`, `requests` 등)

**설치는 `pip` 명령어로:**

```bash
pip install requests
```

- **pip:** 외부 패키지들을 설치하도록 도와주는 파이썬의 **패키지 관리 시스템**.
- **`requirements.txt`:** 협업 시 **개발 환경을 통일**하는 데 큰 도움이 된다. 호환성 이슈가 생길 수 있으므로 **버전 관리를 잘 기록**해두는 게 중요하다.

```bash
pip freeze > requirements.txt      # 현재 환경 기록
pip install -r requirements.txt    # 기록된 환경 그대로 설치
```

---

## 6. 실습 — `requests` 패키지

**`requests`란?** 파이썬에서 웹에 요청을 보내고 응답을 받는 걸 아주 쉽게 만들어주는 **외부 패키지**.

### 6.1 설치

```bash
pip install requests
```

### 6.2 사용 예시 — 공휴일 정보 API

```python
import requests

# 공휴일 정보 API
url = "https://date.nager.at/api/v3/publicholidays/2025/KR"
response = requests.get(url).json()
print(response)
```

| 메서드 | 설명 |
|--------|------|
| `.get(url)` | 주어진 url로 요청하는 `requests` 패키지 메서드 |
| `.json()` | 응답 본문(문자열)에 담긴 JSON 데이터를 대응하는 **파이썬 객체(dict, list 등)로 변환**해주는 응답(Response) 객체의 메서드 |

### 6.3 `pprint` — 예쁘게 출력하기

응답 데이터가 크고 중첩되어 있어 `print()`로는 보기 힘들 때, 표준 라이브러리의 **pretty print**를 쓰면 읽기 좋게 정리해준다.

```python
from pprint import pprint

pprint(response)   # 들여쓰기·줄바꿈이 적용되어 읽기 편함
```

> **※ 메서드는 OOP에서 다룰 예정.** 지금은 일단 **함수라고 생각하고** 넘어가면 된다.
