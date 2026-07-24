# Python 데이터 구조 2

> **비시퀀스 자료형: Dictionary, `defaultdict`, Set, Hash Table**

## 목차

1. [비시퀀스 데이터 구조란?](#1-비시퀀스-데이터-구조란)
2. [시퀀스와 비시퀀스 비교](#2-시퀀스와-비시퀀스-비교)
3. [딕셔너리](#3-딕셔너리-dictionary)
4. [딕셔너리 메서드](#4-딕셔너리-메서드)
5. [`defaultdict`](#5-딕셔너리의-확장-defaultdict)
6. [세트](#6-세트-set)
7. [세트의 집합 연산](#7-세트의-집합-연산)
8. [해시 테이블](#8-참고-해시-테이블-hash-table)
9. [해시 가능성](#9-해시-가능성-hashability)
10. [핵심 요약](#10-핵심-요약)

---

## 1. 비시퀀스 데이터 구조란?

이번 장에서는 다음 내용을 다룬다.

- 딕셔너리(`dict`)
- `defaultdict`
- 세트(`set`)
- 세트 메서드와 집합 연산
- 해시 테이블
- 해시 가능성

### 왜 필요한가?

> 친구의 전화번호를 쉽게 찾을 수 있는 구조로 바꿔보자.

비시퀀스 자료형을 활용하면 다음과 같은 장점이 있다.

- **키-값(key-value) 구조**를 활용해 데이터를 빠르게 찾을 수 있다.
- 인덱스 대신 의미 있는 키를 사용해 코드의 **가독성과 직관성**을 높일 수 있다.
- 적절한 자료구조를 선택하면 코드의 **성능과 유지보수성**을 개선할 수 있다.

```python
# 인덱스를 사용하는 경우
phone_numbers[0]

# 의미 있는 키를 사용하는 경우
phonebook['민수']
```

---

## 2. 시퀀스와 비시퀀스 비교

| 구분 | 시퀀스(Sequence) | 비시퀀스(Non-sequence) |
|---|---|---|
| 대표 자료형 | `str`, `list`, `tuple`, `range` | `dict`, `set` |
| 데이터를 찾는 기준 | 위치 또는 인덱스 | 딕셔너리의 키 또는 세트의 요소 |
| 접근 예시 | `books[0]` | `phonebook['민수']` |
| 슬라이싱 | 가능 | 불가능 |
| 중복 | 일반적으로 허용 | 딕셔너리의 키와 세트의 요소는 중복 불가 |
| 순서 | 순서가 있음 | 딕셔너리는 삽입 순서를 유지하지만 세트는 순서를 보장하지 않음 |

### 인덱스를 사용하지 않으면 무엇이 좋을까?

리스트에서 특정 사람의 전화번호를 찾으려면 각 항목을 순서대로 확인해야 할 수 있다.

반면 딕셔너리는 사람의 이름을 키로 사용한다.

```python
phonebook = {
    '민수': '010-1234-5678',
    '지수': '010-9876-5432',
}

print(phonebook['민수'])
```

딕셔너리는 내부적으로 **해시 테이블**을 사용하기 때문에 키를 이용한 검색·삽입·삭제를 평균적으로 매우 빠르게 수행한다.

> 딕셔너리와 세트의 검색·삽입·삭제는 일반적으로 평균 `O(1)`이다.  
> 다만 해시 충돌 등 특수한 상황에서는 최악의 경우 `O(n)`이 될 수 있다.

---

## 3. 딕셔너리(Dictionary)

딕셔너리는 데이터를 **키와 값의 쌍**으로 저장하는 자료구조다.

```python
student = {
    'name': '민수',
    'age': 20,
    'major': 'Computer Science',
}
```

딕셔너리는 내부적으로 **해시 테이블(Hash Table)**을 사용해 키-값 쌍을 관리한다.

### 딕셔너리의 특징

- 키를 이용한 검색·삽입·삭제가 평균적으로 빠르다.
- 키는 중복될 수 없다.
- 키는 **해시 가능한 객체**여야 한다.
- 값은 중복될 수 있다.
- 값에는 어떤 자료형이든 저장할 수 있다.
- Python 3.7 이상에서는 **삽입 순서가 언어 사양으로 보장**된다.

### 키와 값으로 사용할 수 있는 자료형

```python
data = {
    'name': '민수',       # 문자열 키
    1: 'one',             # 정수 키
    (10, 20): 'point',    # 튜플 키
}
```

딕셔너리의 키는 해시 가능해야 하므로 리스트·딕셔너리·세트와 같은 기본 가변 컨테이너는 키로 사용할 수 없다.

```python
data = {}

data[[1, 2, 3]] = 'value'
# TypeError: unhashable type: 'list'
```

### 다른 언어와 비교

파이썬의 `dict`는 다른 언어의 `Map`, `HashMap` 등과 개념적으로 비슷하다.

공통된 핵심은 다음과 같다.

> 키와 값을 쌍으로 저장하고, 키를 이용해 값을 빠르게 찾는다.

다만 삽입 순서 보장 여부, 키의 타입 제약, 내부 구현 방식 등은 언어마다 다를 수 있다.

---

## 4. 딕셔너리 메서드

⭐ 표시는 자주 사용하는 핵심 메서드다.

| 메서드 | 설명 |
|---|---|
| ⭐ `D.get(k)` | 키 `k`의 값을 반환한다. 키가 없으면 `None`을 반환한다. |
| `D.get(k, default)` | 키 `k`의 값을 반환한다. 키가 없으면 `default`를 반환한다. |
| ⭐ `D.keys()` | 딕셔너리의 키를 모은 뷰 객체를 반환한다. |
| ⭐ `D.values()` | 딕셔너리의 값을 모은 뷰 객체를 반환한다. |
| ⭐ `D.items()` | 딕셔너리의 키-값 쌍을 모은 뷰 객체를 반환한다. |
| `D.setdefault(k)` | 키 `k`의 값을 반환한다. 키가 없으면 `k: None`을 추가하고 `None`을 반환한다. |
| `D.setdefault(k, default)` | 키가 없으면 `k: default`를 추가하고 `default`를 반환한다. |
| ⭐ `D.update(other)` | 다른 매핑이나 키-값 쌍으로 딕셔너리를 갱신한다. 기존 키는 덮어쓴다. |
| ⭐ `D.pop(k)` | 키 `k`를 제거하고 연결된 값을 반환한다. 키가 없으면 `KeyError`가 발생한다. |
| `D.pop(k, default)` | 키 `k`를 제거하고 값을 반환한다. 키가 없으면 `default`를 반환한다. |
| ⭐ `D.clear()` | 딕셔너리의 모든 키-값 쌍을 제거한다. |

---

### 4.1. `get()`

`get()`은 키가 존재하지 않아도 오류를 발생시키지 않고 값을 조회할 수 있게 해준다.

```python
some_dict = {'a': 1, 'b': 2}

some_dict['c']
# KeyError: 'c'

some_dict.get('c')
# None

some_dict.get('c', 0)
# 0
```

대괄호 접근과 `get()`은 상황에 따라 선택한다.

- 키가 반드시 존재해야 한다면 `D[key]`
- 키가 없을 수도 있다면 `D.get(key)`
- 키가 없을 때 기본값이 필요하다면 `D.get(key, default)`

```python
user = {'name': '민수'}

# 반드시 있어야 하는 데이터
name = user['name']

# 없을 수도 있는 데이터
age = user.get('age')

# 없으면 기본값 사용
city = user.get('city', '미입력')
```

> 키가 반드시 존재해야 하는 상황에서 `get()`을 사용하면 오류를 발견하지 못하고 `None`이 전달될 수 있다. 따라서 무조건 `get()`이 더 안전한 것은 아니다.

---

### 4.2. `keys()`, `values()`, `items()`

세 메서드는 모두 리스트가 아닌 **딕셔너리 뷰(view) 객체**를 반환한다.

```python
d = {'a': 1, 'b': 2}

print(d.keys())
# dict_keys(['a', 'b'])

print(d.values())
# dict_values([1, 2])

print(d.items())
# dict_items([('a', 1), ('b', 2)])
```

반복문에서는 다음과 같이 사용할 수 있다.

```python
d = {'a': 1, 'b': 2}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)
```

딕셔너리를 직접 순회하면 기본적으로 키를 순회한다.

```python
for key in d:
    print(key)
```

`items()`의 각 요소는 키와 값으로 구성된 튜플처럼 동작하므로 구조 분해 할당을 사용할 수 있다.

```python
for key, value in d.items():
    print(f'{key}: {value}')
```

---

### 4.3. `setdefault()`

`setdefault()`는 키에 연결된 값을 반환한다.

키가 없다면 해당 키와 기본값을 딕셔너리에 추가한 뒤 기본값을 반환한다.

```python
d = {'a': 1}

result1 = d.setdefault('a', 100)
print(result1)
# 1

result2 = d.setdefault('b', 100)
print(result2)
# 100

print(d)
# {'a': 1, 'b': 100}
```

리스트를 값으로 사용하는 그룹화 작업에도 활용할 수 있다.

```python
fruits = [
    ('red', 'apple'),
    ('yellow', 'banana'),
    ('red', 'cherry'),
]

fruit_by_color = {}

for color, fruit in fruits:
    fruit_by_color.setdefault(color, []).append(fruit)

print(fruit_by_color)
# {'red': ['apple', 'cherry'], 'yellow': ['banana']}
```

> `setdefault()`는 딕셔너리를 직접 변경한다. 값을 조회만 하려는 경우에는 `get()`을 사용하는 것이 적절하다.

---

### 4.4. `update()`

`update()`는 다른 딕셔너리나 키-값 쌍을 이용해 딕셔너리를 갱신한다.

기존 키는 새로운 값으로 덮어쓰고, 존재하지 않는 키는 새로 추가한다.

```python
d = {'a': 1, 'b': 2}

d.update({'b': 20, 'c': 3})

print(d)
# {'a': 1, 'b': 20, 'c': 3}
```

키워드 인자도 사용할 수 있다.

```python
d.update(d=4, e=5)

print(d)
# {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5}
```

키-값 쌍으로 구성된 이터러블도 전달할 수 있다.

```python
d.update([('f', 6), ('g', 7)])

print(d)
# {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
```

---

### 4.5. `pop()`

`pop()`은 키를 제거하고 해당 키에 연결된 값을 반환한다.

```python
d = {'a': 1, 'b': 2}

value = d.pop('a')

print(value)
# 1

print(d)
# {'b': 2}
```

키가 없으면 `KeyError`가 발생한다.

```python
d.pop('z')
# KeyError: 'z'
```

기본값을 지정하면 키가 없어도 오류가 발생하지 않는다.

```python
result = d.pop('z', '없음')

print(result)
# 없음
```

> 리스트의 `pop()`과 달리 딕셔너리의 `pop()`에는 제거할 키를 반드시 전달해야 한다.

```python
d.pop()
# TypeError
```

딕셔너리의 마지막 키-값 쌍을 제거하려면 `popitem()`을 사용할 수 있다.

```python
d = {'a': 1, 'b': 2}

item = d.popitem()

print(item)
# ('b', 2)

print(d)
# {'a': 1}
```

---

### 4.6. `clear()`

`clear()`는 딕셔너리의 모든 키-값 쌍을 제거한다.

```python
d = {'a': 1, 'b': 2}

d.clear()

print(d)
# {}
```

---

## 5. 딕셔너리의 확장: `defaultdict`

`defaultdict`는 파이썬 표준 라이브러리의 `collections` 모듈에서 제공하는 딕셔너리 자료형이다.

```python
from collections import defaultdict
```

존재하지 않는 키를 대괄호로 조회하면 지정된 함수를 호출해 기본값을 자동으로 생성한다.

```python
from collections import defaultdict

d = defaultdict(int)

print(d['a'])
# 0
```

### `defaultdict`의 특징

- 존재하지 않는 키에 자동으로 기본값을 생성한다.
- 카운팅과 그룹화 작업에 유용하다.
- 키의 존재 여부를 확인하는 반복 코드를 줄일 수 있다.
- 기본값을 생성할 함수를 `defaultdict()`에 전달한다.

---

### 5.1. 문자 개수 세기

#### 일반 딕셔너리 사용

```python
text = 'banana'
counts = {}

for char in text:
    if char not in counts:
        counts[char] = 0

    counts[char] += 1

print(counts)
# {'b': 1, 'a': 3, 'n': 2}
```

#### `defaultdict` 사용

```python
from collections import defaultdict

text = 'banana'
counts = defaultdict(int)

for char in text:
    counts[char] += 1

print(counts)
# defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})
```

`int()`는 인자 없이 호출하면 `0`을 반환한다.

```python
print(int())
# 0
```

따라서 `defaultdict(int)`는 존재하지 않는 키의 기본값을 `0`으로 생성한다.

---

### 5.2. 색깔별 과일 분류하기

```python
from collections import defaultdict

fruits = [
    ('red', 'apple'),
    ('yellow', 'banana'),
    ('red', 'cherry'),
]

fruit_by_color = defaultdict(list)

for color, fruit in fruits:
    fruit_by_color[color].append(fruit)

print(fruit_by_color)
# defaultdict(
#     <class 'list'>,
#     {'red': ['apple', 'cherry'], 'yellow': ['banana']}
# )
```

`list()`는 인자 없이 호출하면 빈 리스트를 반환한다.

```python
print(list())
# []
```

따라서 존재하지 않는 색상 키에 접근하면 빈 리스트가 만들어지고, 곧바로 `append()`를 호출할 수 있다.

---

### 5.3. 자주 사용하는 패턴

| 패턴 | 초기화 | 기본값 | 주요 용도 |
|---|---|---|---|
| 숫자 세기 | `defaultdict(int)` | `0` | 빈도수 계산, 카운팅 |
| 리스트로 그룹화 | `defaultdict(list)` | `[]` | 데이터 분류, 인접 리스트 |
| 세트로 그룹화 | `defaultdict(set)` | `set()` | 중복 없는 데이터 분류 |

```python
from collections import defaultdict

graph = defaultdict(list)

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
]

for start, end in edges:
    graph[start].append(end)

print(graph)
# defaultdict(<class 'list'>, {'A': ['B', 'C'], 'B': ['D']})
```

`defaultdict(list)`는 그래프의 인접 리스트를 구성하거나 데이터를 그룹별로 분류할 때 특히 유용하다.

---

### 5.4. 주의: 조회만 해도 키가 생성될 수 있다

존재하지 않는 키를 대괄호로 조회하면 키가 실제로 추가된다.

```python
from collections import defaultdict

d = defaultdict(int)

print(d['x'])
# 0

print(d)
# defaultdict(<class 'int'>, {'x': 0})
```

키를 생성하지 않고 존재 여부만 확인하려면 `in` 연산자를 사용한다.

```python
print('y' in d)
# False

print(d)
# defaultdict(<class 'int'>, {'x': 0})
```

`get()`도 기본값 생성 함수를 호출하지 않는다.

```python
print(d.get('z'))
# None

print(d)
# defaultdict(<class 'int'>, {'x': 0})
```

> `defaultdict`의 기본값 생성은 존재하지 않는 키를 `d[key]` 형태로 조회할 때 발생한다.

---

## 6. 세트(Set)

세트는 **중복되지 않는 요소**를 저장하는 자료구조다.

```python
numbers = {1, 2, 3, 4}
```

세트도 딕셔너리처럼 내부적으로 해시 테이블을 사용한다.

### 세트의 특징

- 중복을 허용하지 않는다.
- 요소의 순서를 보장하지 않는다.
- 인덱싱과 슬라이싱을 지원하지 않는다.
- 요소는 해시 가능해야 한다.
- 요소 추가·삭제·존재 여부 확인이 평균적으로 빠르다.
- 합집합·교집합·차집합 등의 집합 연산을 지원한다.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
# {1, 2, 3}
```

### 빈 세트 만들기

빈 중괄호 `{}`는 딕셔너리를 의미한다.

```python
empty_dict = {}
print(type(empty_dict))
# <class 'dict'>
```

빈 세트는 반드시 `set()`으로 만든다.

```python
empty_set = set()
print(type(empty_set))
# <class 'set'>
```

---

### 6.1. 세트 메서드

| 메서드 | 설명 |
|---|---|
| ⭐ `s.add(x)` | 요소 `x`를 추가한다. 이미 존재하면 변화가 없다. |
| ⭐ `s.update(iterable)` | 이터러블의 모든 요소를 세트에 추가한다. |
| `s.clear()` | 모든 요소를 제거한다. |
| ⭐ `s.remove(x)` | 요소 `x`를 제거한다. 요소가 없으면 `KeyError`가 발생한다. |
| ⭐ `s.discard(x)` | 요소 `x`를 제거한다. 요소가 없어도 오류가 발생하지 않는다. |
| `s.pop()` | 임의의 요소 하나를 제거하고 반환한다. |

---

### 6.2. `add()`

`add()`는 세트에 요소 하나를 추가한다.

```python
s = {1, 2, 3}

s.add(4)

print(s)
# {1, 2, 3, 4}
```

이미 존재하는 요소를 추가하면 아무 변화도 없다.

```python
s.add(4)

print(s)
# {1, 2, 3, 4}
```

> 세트의 출력 순서는 보장되지 않는다. 위 출력 순서는 실행 환경에 따라 다르게 보일 수 있다.

---

### 6.3. `update()`

`update()`는 이터러블의 요소를 하나씩 꺼내 세트에 추가한다.

```python
s = {1, 2}

s.update([3, 4, 5])

print(s)
# {1, 2, 3, 4, 5}
```

여러 이터러블을 한 번에 전달할 수도 있다.

```python
s = {1, 2}

s.update([3, 4], (5, 6), {7, 8})

print(s)
# {1, 2, 3, 4, 5, 6, 7, 8}
```

문자열도 이터러블이므로 각 문자가 개별 요소로 추가된다.

```python
s = set()

s.update('abc')

print(s)
# {'a', 'b', 'c'}
```

`add()`와 `update()`의 차이를 구분해야 한다.

```python
s = set()

s.add('abc')
print(s)
# {'abc'}

s = set()

s.update('abc')
print(s)
# {'a', 'b', 'c'}
```

---

### 6.4. `clear()`

`clear()`는 세트의 모든 요소를 제거한다.

```python
s = {1, 2, 3}

s.clear()

print(s)
# set()
```

---

### 6.5. `remove()`와 `discard()`

두 메서드 모두 세트에서 특정 요소를 제거한다.

차이는 요소가 존재하지 않을 때의 동작이다.

```python
s = {1, 2, 3}

s.remove(1)

print(s)
# {2, 3}
```

`remove()`는 요소가 없으면 `KeyError`를 발생시킨다.

```python
s.remove(100)
# KeyError: 100
```

`discard()`는 요소가 없어도 오류를 발생시키지 않는다.

```python
s = {1, 2, 3}

s.discard(2)
s.discard(100)

print(s)
# {1, 3}
```

#### 어떤 메서드를 사용해야 할까?

| 상황 | 권장 메서드 |
|---|---|
| 요소가 반드시 존재해야 함 | `remove()` |
| 요소가 없어도 정상적인 상황임 | `discard()` |
| 요소가 없는 것이 버그일 수 있음 | `remove()` |
| 존재 여부와 관계없이 제거하고 싶음 | `discard()` |

> `discard()`가 항상 더 안전한 것은 아니다. 요소가 반드시 있어야 하는 상황에서는 `remove()`를 사용해야 문제를 빠르게 발견할 수 있다.

---

### 6.6. `pop()`

`pop()`은 세트에서 임의의 요소 하나를 제거하고 반환한다.

```python
s = {1, 2, 3}

value = s.pop()

print(value)
print(s)
```

세트는 순서를 보장하지 않으므로 어떤 요소가 제거될지 의존해서는 안 된다.

```python
s = set()

s.pop()
# KeyError: 'pop from an empty set'
```

> 세트의 `pop()`이 반환하는 요소는 임의의 요소다. 무작위로 선택한다는 의미가 아니라, 개발자가 반환 순서를 예측하거나 의존할 수 없다는 의미다.

---

## 7. 세트의 집합 연산

세트는 수학의 집합 연산을 메서드와 연산자 형태로 제공한다.

| 연산 | 메서드 | 연산자 | 의미 |
|---|---|:---:|---|
| 차집합 | `set1.difference(set2)` | `set1 - set2` | `set1`에는 있지만 `set2`에는 없는 요소 |
| 교집합 | `set1.intersection(set2)` | `set1 & set2` | 두 세트에 모두 존재하는 요소 |
| 합집합 | `set1.union(set2)` | `set1 \| set2` | 두 세트 중 하나 이상에 존재하는 요소 |
| 대칭 차집합 | `set1.symmetric_difference(set2)` | `set1 ^ set2` | 한쪽 세트에만 존재하는 요소 |
| 부분집합 | `set1.issubset(set2)` | `set1 <= set2` | `set1`의 모든 요소가 `set2`에 포함되는지 확인 |
| 진부분집합 | — | `set1 < set2` | 부분집합이면서 두 세트가 서로 다른지 확인 |
| 상위집합 | `set1.issuperset(set2)` | `set1 >= set2` | `set1`이 `set2`의 모든 요소를 포함하는지 확인 |
| 진상위집합 | — | `set1 > set2` | 상위집합이면서 두 세트가 서로 다른지 확인 |
| 서로소 | `set1.isdisjoint(set2)` | — | 공통 요소가 없는지 확인 |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

### 차집합

```python
print(a.difference(b))
# {1, 2}

print(a - b)
# {1, 2}
```

### 교집합

```python
print(a.intersection(b))
# {3, 4}

print(a & b)
# {3, 4}
```

### 합집합

```python
print(a.union(b))
# {1, 2, 3, 4, 5, 6}

print(a | b)
# {1, 2, 3, 4, 5, 6}
```

### 대칭 차집합

```python
print(a.symmetric_difference(b))
# {1, 2, 5, 6}

print(a ^ b)
# {1, 2, 5, 6}
```

### 부분집합

```python
small = {1, 2}

print(small.issubset(a))
# True

print(small <= a)
# True
```

### 상위집합

```python
print(a.issuperset(small))
# True

print(a >= small)
# True
```

### 서로소

```python
x = {1, 2}
y = {3, 4}

print(x.isdisjoint(y))
# True
```

> 연산자는 표현이 간결하고 수학적 표기와 유사하다. 메서드는 연산의 의미를 이름으로 명확하게 나타낼 수 있다. 상황과 팀의 코드 스타일에 따라 선택하면 된다.

---

## 8. 참고: 해시 테이블(Hash Table)

해시 테이블은 키와 값을 연결해 저장하고, 키를 이용해 데이터를 빠르게 찾는 자료구조다.

파이썬의 딕셔너리와 세트는 내부적으로 해시 테이블을 사용한다.

### 도서관에서 책 찾기

> 수만 권의 책이 있는 도서관에서 원하는 책을 찾는다고 생각해 보자.
>
> 책을 처음부터 하나씩 확인하면 시간이 오래 걸린다. 하지만 책 제목을 색인으로 변환해 책장의 위치를 알 수 있다면 해당 책장으로 곧바로 이동할 수 있다.

해시 테이블도 이와 비슷하다.

키를 해시값으로 변환하고, 그 결과를 이용해 데이터를 저장하거나 검색할 위치를 결정한다.

---

### 8.1. 해시 테이블의 기본 원리

1. 키를 해시 함수에 전달한다.
2. 해시 함수가 정수 형태의 해시값을 반환한다.
3. 해시값을 이용해 데이터를 저장할 위치를 결정한다.
4. 같은 키를 검색할 때 다시 해시값을 계산한다.
5. 계산된 위치로 이동해 데이터를 찾는다.

```text
키
↓
해시 함수
↓
해시값
↓
해시 테이블의 저장 위치
↓
값
```

이러한 방식 덕분에 딕셔너리와 세트의 검색·삽입·삭제는 평균적으로 `O(1)`에 수행된다.

---

### 8.2. 해시(Hash)란?

해시는 데이터를 정수 형태의 값으로 변환한 결과다.

```python
print(hash('apple'))
print(hash(42))
print(hash((1, 2)))
```

해시값은 데이터를 빠르게 분류하고 저장 위치를 결정하는 데 사용된다.

다만 서로 다른 데이터가 같은 해시값을 가질 수도 있다.

```text
서로 다른 입력
↓
같은 해시값
```

이를 **해시 충돌(Hash Collision)**이라고 한다.

> 해시값은 데이터의 고유한 식별자가 아니다. 서로 다른 객체가 같은 해시값을 가질 수 있다.

파이썬의 딕셔너리와 세트는 해시 충돌이 발생해도 실제 객체의 동등성까지 확인해 올바른 데이터를 찾는다.

---

### 8.3. 해시 함수(Hash Function)

해시 함수는 객체를 입력받아 정수 형태의 해시값을 반환한다.

파이썬에서는 내장 함수 `hash()`를 사용해 객체의 해시값을 확인할 수 있다.

```python
hash('apple')
hash(42)
hash((1, 2))
```

모든 객체에 `hash()`를 사용할 수 있는 것은 아니다.

```python
hash([1, 2, 3])
# TypeError: unhashable type: 'list'
```

해시 가능한 객체만 딕셔너리의 키 또는 세트의 요소로 사용할 수 있다.

---

### 8.4. 해시 테이블이 빠른 이유

리스트에서 특정 값을 찾으려면 앞에서부터 각 요소를 비교해야 할 수 있다.

```python
numbers = [10, 20, 30, 40, 50]

print(40 in numbers)
```

이 경우 데이터가 많아질수록 확인해야 하는 요소의 수가 늘어날 수 있다.

반면 딕셔너리와 세트는 해시값을 이용해 데이터가 있을 것으로 예상되는 위치로 바로 이동한다.

```python
numbers = {10, 20, 30, 40, 50}

print(40 in numbers)
```

평균 시간 복잡도는 다음과 같다.

| 연산 | 리스트 | 딕셔너리·세트 |
|---|:---:|:---:|
| 요소 검색 | `O(n)` | 평균 `O(1)` |
| 요소 추가 | 상황에 따라 다름 | 평균 `O(1)` |
| 요소 삭제 | 일반적으로 `O(n)` | 평균 `O(1)` |

> 해시 테이블의 연산이 항상 `O(1)`인 것은 아니다. 해시 충돌이 많이 발생하거나 테이블의 크기를 조정하는 상황에서는 더 많은 시간이 필요할 수 있다.

---

### 8.5. 세트의 저장 원리

세트는 각 요소의 해시값을 계산해 해시 테이블에 저장한다.

```text
요소
↓
해시 함수
↓
해시값
↓
해시 테이블의 위치
```

세트의 요소는 입력 순서가 아니라 내부 해시 테이블의 배치에 따라 관리된다.

따라서 다음과 같은 특징이 나타난다.

- 입력 순서를 보장하지 않는다.
- 인덱싱할 수 없다.
- `pop()`으로 어떤 요소가 제거될지 의존할 수 없다.
- 출력 순서가 실행 환경에 따라 다르게 보일 수 있다.

---

### 8.6. 딕셔너리와 세트의 순서 차이

#### 딕셔너리

Python 3.7 이상에서는 딕셔너리의 삽입 순서가 언어 사양으로 보장된다.

```python
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)
# {'a': 1, 'b': 2, 'c': 3}
```

#### 세트

세트는 삽입 순서를 보장하지 않는다.

```python
s = set()

s.add('a')
s.add('b')
s.add('c')

print(s)
# 출력 순서는 보장되지 않음
```

> 딕셔너리도 내부적으로 해시 테이블을 사용하지만, 삽입 순서를 유지하기 위한 구조를 함께 관리한다.

---

### 8.7. 문자열의 해시값은 실행마다 달라질 수 있다

문자열과 바이트열 등 일부 자료형에는 **해시 난수화(Hash Randomization)**가 적용된다.

```python
print(hash('apple'))
```

같은 파이썬 프로세스 안에서는 같은 문자열의 해시값이 일관되게 유지된다.

```python
print(hash('apple'))
print(hash('apple'))
# 같은 실행 안에서는 동일한 값
```

하지만 파이썬 프로그램을 종료한 뒤 다시 실행하면 해시값이 달라질 수 있다.

```text
첫 번째 실행: hash('apple') → A
두 번째 실행: hash('apple') → B
```

해시 난수화는 의도적으로 많은 해시 충돌을 발생시키는 공격을 어렵게 만들기 위한 보안 기능이다.

> 해시값을 파일이나 데이터베이스에 저장해 영구 식별자로 사용해서는 안 된다.

---

### 8.8. 해시값은 언제 계산될까?

해시값은 `hash()`를 호출하거나 딕셔너리·세트가 객체를 저장하고 검색하는 과정에서 필요할 때 계산된다.

```python
key = 'apple'

hash(key)       # 직접 해시값 요청

d = {key: 10}  # 딕셔너리에 저장할 때 해시값 필요

print(d[key])   # 키를 검색할 때 해시값 필요
```

정확한 내부 계산 및 캐싱 방식은 객체의 종류와 파이썬 구현에 따라 달라질 수 있다.

---

## 9. 해시 가능성(Hashability)

해시 가능한 객체는 다음 조건을 만족해야 한다.

1. `hash()`를 호출할 수 있어야 한다.
2. 객체가 해시 테이블에 저장된 동안 해시값이 변하지 않아야 한다.
3. 두 객체가 같다면 해시값도 같아야 한다.

```python
a = 'apple'
b = 'apple'

print(a == b)
# True

print(hash(a) == hash(b))
# True
```

반대는 반드시 성립하지 않는다.

```text
해시값이 같다고 해서 두 객체가 반드시 같은 것은 아니다.
```

해시 충돌이 발생할 수 있기 때문이다.

---

### 9.1. 어떤 객체가 해시 가능한가?

대표적인 해시 가능 객체는 다음과 같다.

- `int`
- `float`
- `bool`
- `str`
- `bytes`
- `frozenset`
- 해시 가능한 요소로만 구성된 `tuple`

```python
hash(10)
hash(3.14)
hash('hello')
hash((1, 2, 3))
hash(frozenset({1, 2, 3}))
```

기본 가변 컨테이너는 일반적으로 해시할 수 없다.

- `list`
- `dict`
- `set`

```python
hash([1, 2, 3])
# TypeError: unhashable type: 'list'

hash({'a': 1})
# TypeError: unhashable type: 'dict'

hash({1, 2, 3})
# TypeError: unhashable type: 'set'
```

---

### 9.2. 튜플은 항상 해시 가능할까?

튜플 자체는 불변 자료형이지만, 내부 요소가 모두 해시 가능해야 튜플도 해시할 수 있다.

```python
hash((1, 2, 3))
# 정상 실행
```

내부에 리스트가 포함되어 있으면 해시할 수 없다.

```python
hash((1, [2, 3]))
# TypeError: unhashable type: 'list'
```

```python
valid_key = (1, 2, 3)

d = {
    valid_key: 'value',
}
```

```python
invalid_key = (1, [2, 3])

d = {
    invalid_key: 'value',
}
# TypeError
```

> 컨테이너가 불변이라는 사실만으로 충분하지 않다. 컨테이너 내부의 모든 요소도 해시 가능해야 한다.

---

### 9.3. 가변 컨테이너는 왜 해시할 수 없을까?

해시 테이블은 객체의 해시값을 이용해 데이터를 저장할 위치를 결정한다.

```text
객체
↓
해시값
↓
저장 위치
```

만약 객체의 내용이 변경되어 해시값까지 달라진다면 다음과 같은 문제가 발생할 수 있다.

1. 변경 전 해시값을 이용해 데이터를 저장한다.
2. 객체의 내용이 변경된다.
3. 변경 후 해시값이 달라진다.
4. 검색 시 새로운 위치를 확인한다.
5. 원래 저장된 데이터를 찾지 못한다.

개념적으로 표현하면 다음과 같다.

```text
저장할 때의 위치: A
변경 후 검색 위치: B
```

따라서 리스트·딕셔너리·세트와 같은 기본 가변 컨테이너는 딕셔너리의 키나 세트의 요소로 사용할 수 없다.

```python
d = {}
key = [1, 2, 3]

d[key] = 'value'
# TypeError: unhashable type: 'list'
```

> 해시 테이블은 객체의 해시값이 저장된 동안 변하지 않는다는 전제에 의존한다.

---

### 9.4. 세트를 딕셔너리의 키로 사용하고 싶다면?

일반 세트는 가변이므로 해시할 수 없다.

```python
hash({1, 2, 3})
# TypeError: unhashable type: 'set'
```

대신 불변 세트인 `frozenset`을 사용할 수 있다.

```python
key = frozenset({1, 2, 3})

d = {
    key: 'value',
}

print(d[key])
# value
```

`frozenset`은 요소를 추가하거나 제거할 수 없는 불변 자료형이다.

```python
s = frozenset({1, 2, 3})

s.add(4)
# AttributeError
```

단, `frozenset`의 내부 요소도 모두 해시 가능해야 한다.

---

## 10. 핵심 요약

### 딕셔너리

- 데이터를 키-값 쌍으로 저장한다.
- 키는 중복될 수 없으며 해시 가능해야 한다.
- 값은 어떤 자료형이든 사용할 수 있다.
- 키를 이용한 검색·삽입·삭제는 평균 `O(1)`이다.
- Python 3.7 이상에서는 삽입 순서를 유지한다.

```python
student = {
    'name': '민수',
    'age': 20,
}
```

### `defaultdict`

- 존재하지 않는 키를 조회할 때 기본값을 자동으로 생성한다.
- 카운팅에는 `defaultdict(int)`를 자주 사용한다.
- 그룹화에는 `defaultdict(list)`를 자주 사용한다.
- 대괄호 조회만으로 키가 생성될 수 있으므로 주의해야 한다.

```python
from collections import defaultdict

counts = defaultdict(int)
groups = defaultdict(list)
```

### 세트

- 중복되지 않는 요소를 저장한다.
- 요소는 해시 가능해야 한다.
- 순서를 보장하지 않는다.
- 검색·삽입·삭제는 평균 `O(1)`이다.
- 합집합·교집합·차집합 등의 집합 연산을 지원한다.

```python
numbers = {1, 2, 3}
```

### 해시 테이블

- 키나 요소의 해시값을 이용해 저장 위치를 결정한다.
- 평균적으로 빠른 검색·삽입·삭제를 제공한다.
- 서로 다른 객체가 같은 해시값을 가질 수 있으며, 이를 해시 충돌이라고 한다.
- 해시값은 영구적인 식별자로 사용하면 안 된다.

### 해시 가능성

- 딕셔너리의 키와 세트의 요소는 해시 가능해야 한다.
- 기본 가변 컨테이너인 `list`, `dict`, `set`은 해시할 수 없다.
- 튜플은 내부의 모든 요소가 해시 가능할 때만 해시할 수 있다.
- 불변 세트가 필요하다면 `frozenset`을 사용할 수 있다.

```python
hash((1, 2, 3))          # 가능
hash((1, [2, 3]))         # 불가능
hash(frozenset({1, 2}))   # 가능
```
