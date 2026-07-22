# Python 제어문 정리 (Control of Flow)

## 1. 제어문이란?

상황에 따라 **다른 코드를 실행**하거나, 같은 코드를 **여러 번 반복**하는 구문.
조건에 따라 코드 블록을 실행하거나, 반복적으로 코드를 실행한다.

| 분류 | 키워드 |
|------|--------|
| **조건문** | `if`, `elif`, `else` |
| **반복문** | `for`, `while` |

- `for`문은 **`in` 키워드**와 함께 쓴다.
- `while`문은 **단독**으로 조건식과 함께 쓴다.

---

## 2. 조건문 (Conditional Statement)

주어진 **조건식을 평가**해서 `True`일 때만 코드 블록을 실행하고, 아니면 건너뛴다.

### 2.1 기본 구조

```python
# 조건 작성은 반드시 '표현식'

if 조건1:
    조건1을 만족할 때 실행할 코드
elif 조건2:
    조건2를 만족할 때 실행할 코드
elif 조건3:
    조건3을 만족할 때 실행할 코드
else:
    모든 조건을 만족하지 않으면 실행할 코드
```

| 키워드 | 설명 |
|--------|------|
| `if` | 조건문의 기본 형태. 조건은 **표현식**으로 작성 |
| `elif` | 이전 조건을 만족하지 못하고 **추가 조건**이 필요할 때. **여러 개** 사용 가능 |
| `else` | 위의 **모든 조건을 만족하지 않을 때** 실행 |

---

## 3. 복수 조건문 — 순서가 중요하다 ⚠️

- 조건식을 **동시에 검사하는 것이 아니라 "순차적"으로** 비교한다.
- 조건식의 **순서에 따라 원하는 결과가 나오지 않을 수 있음**에 주의.

```python
# ✅ 올바른 순서 — 좁은 조건부터
dust = 155        # 결과: 매우 나쁨

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

```python
# ❌ 잘못된 순서 — 넓은 조건이 앞에
dust = 155        # 결과: 보통 (의도와 다름!)

if dust > 30:     # 155 > 30 → True에서 바로 걸려버림
    print('보통')
elif dust > 80:   # 여기까지 오지도 못함
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')
```

> **핵심:** 위에서부터 순서대로 검사하다가 **처음 True를 만나는 순간 거기서 끝난다.** 범위가 좁고 까다로운 조건을 **위쪽에** 배치해야 한다.

### 3.1 중첩 조건문

조건문 내부에 또 다른 조건문을 작성할 수도 있다.

```python
if age >= 18:
    if has_license:
        print('운전 가능')
    else:
        print('면허 필요')
```

---

## 4. 반복문 (Loop Statement)

주어진 코드 블록을 **여러 번 반복**해서 실행하는 구문.

| 종류 | 특징 |
|------|------|
| `for` | 반복 가능한(iterable) 객체의 요소들을 순회. **반복 횟수가 정해져 있음** |
| `while` | 조건이 **참인 동안** 반복 (= False가 될 때까지). **반복 횟수가 정해지지 않은 경우** |

```python
# for문
student_list = ['Alice', 'Bob', 'Charlie']

for student in student_list:
    print(f"Hello, {student}!")
```

```python
# while문
count = 1

while count <= 3:
    print(count)
    count = count + 1

print('끝')
```

---

## 5. for문 자세히 보기

### 5.1 반복 가능한 객체 (Iterable)

**요소를 하나씩 반환할 수 있는 모든 객체.**

| 분류 | 타입 |
|------|------|
| 시퀀스 | `list`, `tuple`, `str` |
| 비시퀀스 | `dict`, `set` |
| 기타 | `range` 등 |

### 5.2 for문 작동 원리

1. 리스트 내 **첫 항목**이 반복 변수에 할당되고 코드 블록이 실행된다.
2. 반복 변수에 **다음 항목**이 할당되고 다시 실행된다.
3. 더 이상 **할당할 값이 없으면** 반복이 종료된다.

> **팁:** 반복 변수는 **단수형**으로 작성하는 것을 권장한다. (`students` → `for student in students`)

### 5.3 문자열 순회

```python
for char in 'hello':
    print(char)     # h e l l o
```

### 5.4 range 순회

`range()`는 연속된 정수 범위의 시퀀스를 생성해주는 파이썬 **내장 함수**.

```python
for i in range(3):
    print(i)        # 0 1 2
```

### 5.5 딕셔너리 순회

- 딕셔너리는 **비시퀀스**라 순서 보장이 어렵다. (다만 작성한 순서대로 출력은 보장된다)
- 그냥 순회하면 **키(key)가 튀어나온다.**

```python
my_dict = {'a': 1, 'b': 2}

for key in my_dict:
    print(key)              # a b

# 키와 값을 같이 꺼내려면
for key, val in my_dict.items():
    print(key, val)         # a 1 / b 2
```

### 5.6 인덱스로 리스트 순회

리스트의 **요소가 아닌 인덱스로 접근**하여 해당 요소들을 변경할 때 쓴다.
인덱스를 사용하면 리스트의 원하는 위치에 있는 값을 **읽거나 변경**할 수 있다.

```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)      # [8, 12, 20, -16, 10]
```

> **왜 이렇게?** `for num in numbers:`로 순회하면 `num`은 값의 **복사된 이름표**일 뿐이라, `num = num * 2`를 해도 **원본 리스트는 안 바뀐다.** 원본을 수정하려면 **인덱스로 접근**해야 한다.

### 5.7 중첩된 반복문

반복문도 중첩할 수 있다.

```python
# 한 겹만 순회 — 안쪽 리스트가 통째로 나옴
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)
"""
['A', 'B']
['c', 'd']
"""

# 두 겹 순회 — 개별 요소까지 도달
for elem in elements:
    for item in elem:
        print(item)
"""
A
B
c
d
"""
```

---

## 6. while문 자세히 보기

주어진 **조건식이 참인 동안** 코드를 반복 실행하고, **False가 될 때까지** 반복한다.

```python
while 조건식:
    코드 블록
```

### 6.1 작동 원리

1. 조건식을 확인 → `True`면 코드 블록 실행, `False`면 반복 종료
2. 블록 실행이 마무리되면 **다시 while 조건식을 확인**

### 6.2 사용자 입력에 따른 반복

```python
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')
```

```
양의 정수를 입력해주세요.: 0
0은 양의 정수가 아닙니다.
양의 정수를 입력해주세요.: -1
음수를 입력했습니다.
양의 정수를 입력해주세요.: 1
잘했습니다!
```

### 6.3 ⚠️ 무한 루프 주의

- **반드시 종료 조건이 필요**하다.
- 반복문 **내부에서 변수 값을 변화**시키는 게 좋다. (위 예시의 마지막 `input()` 줄이 없으면 무한 루프)
- while문이 시작하기 **전에 사용할 변수를 반드시 초기화**해야 오류를 방지할 수 있다.
- 예상치 못한 상황에 대비해 **`break`문을 활용**하면 좋다.

---

## 7. for vs while 비교

| | **for 반복문** | **while 반복문** |
|---|---|---|
| 동작 | iterable 요소를 하나씩 순회하며 반복 | 주어진 조건식이 참(True)인 동안 반복 |
| 유용한 경우 | **반복 횟수가 명확하게 정해져 있는 경우** | **반복 횟수가 불명확하거나** 조건에 따라 반복을 종료해야 할 때 |
| 예시 상황 | · 리스트, 튜플, 문자열 등 시퀀스 형식 처리<br>· `range()`로 일정 횟수만큼 반복 | · 사용자 입력을 받아 특정 조건이 충족될 때까지 반복<br>· 반복 횟수가 미리 정해져 있지 않고 특정 조건이 만족될 때까지 반복 |

---

## 8. 반복 제어 — `break` / `continue`

때때로 반복문의 **일부만 실행**하는 것이 필요하다.

| 키워드 | 동작 |
|--------|------|
| `break` | 해당 키워드를 만나면 **남은 코드를 무시하고 반복을 즉시 종료**. 반복을 끝내야 할 **명확한 조건**이 있을 때 사용 |
| `continue` | 해당 키워드를 만나면 **다음 코드는 무시하고 다음 반복을 수행** |

```python
# break — 3을 만나면 즉시 종료
for i in range(10):
    if i == 3:
        break
    print(i)        # 0 1 2

# continue — 짝수는 건너뛰고 다음 반복
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)        # 1 3
```

> ⚠️ 과도하게 쓰면 **가독성이 떨어지므로** 필요한 상황에만 사용하자.

---

## 9. 빈 코드 블록 — `pass`

**아무 동작도 하지 않음**을 명시적으로 나타내는 키워드.

- 반복 제어가 아니라, **코드의 틀을 유지**하거나 **나중에 내용을 채우기 위한** 용도.
- 코드를 비워두면 오류가 발생하기 때문에 `pass`를 사용한다.
- 반복문뿐만 아니라 **함수, 조건문**에서도 사용 가능하다.

```python
def my_func():
    pass            # 나중에 구현

if condition:
    pass            # 지금은 아무것도 안 함
else:
    print('실행')
```

---

## 10. 유용한 내장 함수 — `map`

```python
map(function, iterable)
```

**고차 함수(higher-order function).** 반복 가능한 데이터 구조의 **모든 요소에 function을 적용**하고, 그 결과값들을 **map object로 묶어서 반환**한다.

> map object는 그대로는 값이 안 보이므로 보통 `list()`로 형변환해서 쓴다. (range의 lazy evaluation과 비슷한 맥락)

### 10.1 활용 1 — 입력값 처리 (SWEA 문제 등)

문자열 `'1 2 3'`이 입력되었을 때:

```python
numbers1 = input().split()
print(numbers1)     # ['1', '2', '3']   ← 전부 문자열!

numbers2 = list(map(int, input().split()))
print(numbers2)     # [1, 2, 3]         ← 정수로 변환됨
```

> `split()`으로 쪼개면 요소가 전부 **문자열**이다. 각 요소에 `int`를 적용해 숫자로 바꾸는 게 `map(int, ...)`의 역할. 알고리즘 문제 입력 처리의 **정석 패턴**이다.

### 10.2 활용 2 — 람다 표현식과 함께

```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

# lambda 미사용 — 함수를 따로 정의
squared1 = list(map(square, numbers))
print(squared1)     # [1, 4, 9, 16, 25]

# lambda 사용 — 즉석에서 정의
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)     # [1, 4, 9, 16, 25]
```

### 10.3 인자가 여러 개일 때는?

- **인자가 하나면** 함수 **이름만** 넘긴다. → `map(int, ...)`, `map(square, ...)`
  (여기서 괄호를 붙여 `map(int(), ...)`라고 쓰면 안 된다. **호출하는 게 아니라 함수 자체를 넘기는 것**이기 때문.)

- **인자가 여러 개일 때는** 두 가지 방법이 있다:

**① iterable을 여러 개 넘기기** — 함수가 받는 인자 개수만큼 iterable을 나열하면, 각 iterable에서 **같은 위치의 요소끼리 짝지어** 전달된다.

```python
a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))
print(result)       # [11, 22, 33]

# 내장 함수도 동일
print(list(map(pow, [2, 3], [3, 2])))   # [8, 9]  (2**3, 3**2)
```

**② 고정값이 필요하면 람다로 감싸기** — 요소마다 변하지 않는 인자는 람다 안에 박아둔다.

```python
# 모든 요소를 2진수 문자열로: int(x, 2)의 두 번째 인자는 고정
binaries = ['101', '110', '111']
result = list(map(lambda x: int(x, 2), binaries))
print(result)       # [5, 6, 7]
```

> **정리:** 인자가 **요소마다 달라지면** iterable을 추가로 넘기고, 인자가 **항상 고정이면** 람다로 감싼다.

---

## 11. (참고) 더 알아볼 키워드

> 이 중에서도 **for-else**와 **enumerate**는 특히 중요하니 꼭 챙겨두자.

### 11.1 모듈 내부 살펴보기

모르는 모듈을 만났을 때 안을 들여다보는 두 가지 방법.

```python
import math

print(dir(math))    # 모듈이 가진 이름(속성·함수)들을 리스트로 반환
help(math)           # 모듈 전체의 사용법을 확인
help(math.sqrt)      # 특정 함수 하나만 콕 집어 확인
```

- `dir()` : 모듈 안에 **무엇이 들어있는지** 이름만 훑어볼 때
- `help()` : 그 이름이 **어떻게 쓰이는지** 독스트링·사용법을 확인할 때

> **추천:** `help()`로도 충분하지만, 실전에서는 **공식 문서**를 보는 쪽이 설명·예시가 더 풍부해서 추천한다.

### 11.2 ⭐ for-else 구문

`for`문이 **`break` 없이 끝까지 정상적으로 완료되었을 때만** `else` 블록이 실행된다.
반대로 **`break`를 만나 반복문이 중간에 종료되면 `else` 블록은 실행되지 않는다.**

```python
# case 1) break 없이 끝까지 완주 → else 실행됨
for i in range(3):
    if i == 5:
        break
else:
    print('break 없이 완주')   # 실행됨
```

```python
# case 2) 중간에 break 발생 → else 실행 안 됨
for i in range(3):
    if i == 1:
        break
else:
    print('break 없이 완주')   # 실행 안 됨 (break로 빠져나갔으므로)
```

> "찾는 게 없었다"를 표현할 때 유용하다. 파이썬 특유의 문법이라 처음엔 낯설다.

### 11.3 ⭐ `enumerate()`

이터러블의 각 요소에 대해 **인덱스와 값을 함께** 반환하는 내장 함수. 순회할 때마다 `(인덱스, 요소)` 형태의 **튜플**을 뱉는다.

```python
fruits = ['apple', 'banana']

for idx, fruit in enumerate(fruits):
    print(idx, fruit)       # 0 apple / 1 banana

# 시작 번호 지정도 가능
for idx, fruit in enumerate(fruits, start=1):
    print(idx, fruit)       # 1 apple / 2 banana
```

> `for i in range(len(fruits))`보다 훨씬 읽기 좋다.

> **💡 궁금증 — 딕셔너리를 `for`문으로 순회할 때 변수 하나로 받으면 왜 키만 나오지? `enumerate()`처럼 (키, 값) 튜플로 나와야 하는 거 아닌가?**
> 별개의 규칙이다. `enumerate()`는 "인덱스 + 요소"를 튜플로 묶어서 반환하도록 **설계된 함수**라 명시적으로 튜플이 나오는 것이고, 딕셔너리는 기본 순회 시 **키만** 내놓도록 정의되어 있다. (딕셔너리 입장에서 값은 `d[key]`로 언제든 다시 찾을 수 있으므로, 순회의 기본 대상이 키인 것.) 키와 값을 함께 튜플로 받고 싶다면 [5.5 딕셔너리 순회](#55-딕셔너리-순회)에서 본 것처럼 `.items()`를 명시적으로 호출해야 한다 → `for key, val in my_dict.items():`.

### 11.4 `zip()`

여러 개의 반복 가능한 데이터 구조를 **같은 위치끼리 짝지어 하나의 튜플로 묶은 뒤**, zip object로 반환하는 함수. (지퍼처럼)

```python
names = ['Alice', 'Bob']
ages = [25, 30]

for name, age in zip(names, ages):
    print(name, age)        # Alice 25 / Bob 30

print(list(zip(names, ages)))   # [('Alice', 25), ('Bob', 30)]
```

- 길이가 다르면 **가장 짧은 쪽을 기준으로** 묶이고, 나머지는 버려진다.
- zip object는 요소 하나하나가 튜플이라 `for a, b in zip(...)`처럼 **바로 언패킹해서 변수에 받을 수 있다.**

#### 행렬 뒤집기(전치, transpose) — `zip(*matrix)`

행과 열을 뒤집어야 할 때 자주 쓰이는 패턴이다.

```python
matrix = [(1, 2, 3), (4, 5, 6)]

transposed = list(zip(*matrix))
print(transposed)   # [(1, 4), (2, 5), (3, 6)]
```

> `*matrix`로 각 행(row)을 언패킹해 `zip()`에 넘기면, `zip()`이 **같은 열(column)의 값들끼리** 묶어준다. `map`에 iterable을 여러 개 넘기는 것과 비슷한 원리다.
