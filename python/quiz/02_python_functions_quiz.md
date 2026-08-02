# 02. 파이썬 함수 — 평가 대비 20문제

> 출제 범위: [02_python_functions.md](../02_python_functions.md)
> 각 문제에 올바른 답안을 생각해봅시다. 정답과 해설은 최하단에 있습니다.

---

### 1. 다음 코드의 실행 결과는?

```python
def greet(name):
    print(f'안녕, {name}')

result = greet('철수')
print(result)
```

a) `안녕, 철수` 출력 후 `None` 출력
b) `안녕, 철수`만 출력
c) `None`만 출력
d) `TypeError`

---

### 2. 다음 함수 정의에 대해, 호출 시 `SyntaxError`가 발생하는 것은?

```python
def introduce(name, age):
    print(f'{name}, {age}살')
```

a) `introduce('철수', 25)`
b) `introduce(age=25, name='철수')`
c) `introduce('철수', age=25)`
d) `introduce(name='철수', 25)`

---

### 3. 다음 코드의 출력 결과는?

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print(default_arg, args, kwargs)

func(1, 2, 3, 4, 5, key1='v1')
```

a) `default (3, 4, 5) {'key1': 'v1'}`
b) `3 (4, 5) {'key1': 'v1'}`
c) `3 (4, 5, 'v1') {}`
d) `TypeError`

---

### 4. 다음 코드의 실행 결과는?

```python
print('a', 'b', sep='-', end='!')
```

a) `a-b!`
b) `a b!`
c) `a-b` 후 줄바꿈
d) `a!b!`

---

### 5. `print()` 함수의 시그니처에 대한 설명으로 옳지 **않은** 것은?

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

a) `*objects`는 가변 인자로 출력할 값의 개수에 제한이 없다
b) `sep`의 기본값은 공백 한 칸이다
c) `end`의 기본값은 빈 문자열이다
d) `file`의 기본값은 `sys.stdout`이다

---

### 6. 재귀 함수에 대한 설명으로 옳지 **않은** 것은?

a) 반드시 종료 조건(base case)을 설정해야 한다
b) 호출이 콜 스택에 쌓이므로 메모리 사용량이 많다
c) 반복문보다 항상 성능이 우수하다
d) 종료 조건이 없거나 잘못되면 스택 오버플로가 발생할 수 있다

---

### 7. 다음 코드의 실행 결과는?

```python
x = 'G'

def outer():
    x = 'E'
    def inner():
        print(x)
    inner()

outer()
```

a) `G`
b) `E`
c) `L`
d) `NameError`

---

### 8. 다음 코드의 실행 결과는?

```python
num = 0

def increment():
    num += 1

increment()
```

a) `num`이 `1`이 된다
b) `num`이 `0`으로 유지된다
c) `UnboundLocalError` 발생
d) `NameError` 발생

---

### 9. 다음 코드에서 `type(result)`의 결과는?

```python
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([3, 1, 5])
```

a) `<class 'tuple'>`
b) `<class 'list'>`
c) `<class 'int'>`
d) `<class 'set'>`

---

### 10. 다음 코드의 실행 결과는?

```python
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(names)
```

a) `alice jane peter`
b) `['alice', 'jane', 'peter']`
c) `TypeError`
d) `None`

---

### 11. 다음 코드의 실행 결과는?

```python
def introduce(name, age):
    print(name, age)

info = {'name': '철수', 'nickname': 25}
introduce(**info)
```

a) `철수 25`
b) `TypeError`
c) `KeyError`
d) `None`

---

### 12. 다음 코드의 실행 결과는?

```python
students = [('지민', 25), ('서준', 20), ('민우', 30)]
print(sorted(students, key=lambda s: s[1])[0])
```

a) `('지민', 25)`
b) `('서준', 20)`
c) `('민우', 30)`
d) `20`

---

### 13. 다음 코드에서 '인자(argument)'에 해당하는 것은?

```python
def add(a, b):
    return a + b

add(3, 5)
```

a) `a`
b) `b`
c) `3`
d) `add`

---

### 14. 다음 중 정의 시 `SyntaxError`가 발생하는 함수는?

a) `def f(a, b=1): ...`
b) `def f(a=1, b): ...`
c) `def f(*args, **kwargs): ...`
d) `def f(a, *args): ...`

---

### 15. 다음 코드의 실행 결과는?

```python
sum = 10
print(sum([1, 2, 3]))
```

a) `6`
b) `10`
c) `TypeError`
d) `NameError`

---

### 16. 독스트링(docstring)에 대한 설명으로 옳지 **않은** 것은?

a) 함수 바디의 맨 앞에 `"""..."""` 형태로 작성한다
b) 필수가 아니라 선택 사항이다
c) IDE에서 함수를 사용할 때 팝업으로 표시된다
d) 독스트링을 작성하지 않으면 함수 정의 시 `SyntaxError`가 발생한다

---

### 17. `return`에 대한 설명으로 옳지 **않은** 것은?

a) `return`문을 만나면 함수의 실행이 즉시 종료된다
b) `return` 뒤에 값을 쓰지 않으면 `None`이 반환된다
c) `return`문이 아예 없는 함수는 반환값 자체가 존재하지 않는다
d) 쉼표로 여러 값을 나열하면 하나의 튜플로 패킹되어 반환된다

---

### 18. 다음 코드의 실행 결과는?

```python
packed = 1, 2, 3
print(type(packed))
```

a) `<class 'list'>`
b) `<class 'tuple'>`
c) `<class 'set'>`
d) `SyntaxError`

---

### 19. `*`와 `**`에 대한 설명으로 옳지 **않은** 것은?

a) 함수 **정의** 시 `*args`는 여러 위치 인자를 하나의 튜플로 받는다
b) 함수 **호출** 시 `*리스트`는 리스트를 개별 위치 인자로 전달한다
c) 함수 **정의** 시 `**kwargs`는 여러 키워드 인자를 하나의 딕셔너리로 받는다
d) 함수 **호출** 시 `**딕셔너리`는 딕셔너리를 하나의 위치 인자로 전달한다

---

### 20. 다음 중 람다(lambda) 표현식을 사용하기에 가장 적절한 상황은?

a) 여러 곳에서 반복적으로 호출되며 복잡한 로직을 담은 함수를 만들 때
b) `sorted()`의 `key`처럼 매개변수가 함수를 요구할 때 일회성으로 기준을 지정할 때
c) 함수에 독스트링을 상세히 작성해야 할 때
d) 재귀 호출로 문제를 분할해서 풀어야 할 때

---
---

## 정답 및 해설

| 번호 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 정답 | a | d | b | a | c | c | b | c | a | c |

| 번호 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 정답 | b | b | c | b | c | d | c | b | d | b |

---

**1. 정답 a)**
`greet` 함수에는 `return`문이 없으므로 파이썬이 자동으로 `None`을 반환한다. 함수 안의 `print()`로 인사말이 먼저 출력되고, 그 반환값인 `None`이 다음 줄에 출력된다. **"출력하는 것"과 "반환하는 것"은 다르다**는 게 핵심.

**2. 정답 d) `introduce(name='철수', 25)`**
호출 시 **키워드 인자는 반드시 위치 인자보다 뒤에** 와야 한다. 이미 키워드로 순서가 깨진 상태에서 위치 인자가 오면 그 값이 몇 번째 자리인지 판단할 수 없기 때문이다.

**3. 정답 b) `3 (4, 5) {'key1': 'v1'}`**
- `1`, `2` → 위치 인자 `pos1`, `pos2`
- `3` → 기본 인자 `default_arg`를 **덮어씀**
- `4, 5` → 남은 위치 인자가 `*args` 튜플로
- `key1='v1'` → `**kwargs` 딕셔너리로

**4. 정답 a) `a-b!`**
`sep`은 값 **사이**의 구분자, `end`는 출력 **끝**에 붙는 문자다. `end='!'`이므로 줄바꿈 대신 `!`가 붙는다.

**5. 정답 c)**
`end`의 기본값은 빈 문자열이 아니라 **줄바꿈(`'\n'`)**이다. 그래서 `print()`가 기본적으로 줄을 바꿔주는 것이다.

**6. 정답 c)**
재귀는 가독성과 표현의 자연스러움이 장점이지만, 호출이 콜 스택에 쌓여 **메모리 사용량이 많고 스택 오버플로 위험**이 있다. 성능이 항상 우수한 것은 아니다.

**7. 정답 b) `E`**
LEGB 규칙에 따라 `inner`는 Local에 `x`가 없으므로 **Enclosed**(감싸는 함수 `outer`)를 먼저 찾는다. `outer`의 `x = 'E'`가 발견되어 Global의 `'G'`까지 가지 않는다.

**8. 정답 c) `UnboundLocalError`**
함수 안에서 `num += 1`처럼 **대입**이 일어나면 파이썬은 `num`을 로컬 변수로 간주한다. 그런데 `num = num + 1`은 대입 전에 값을 **참조**하므로, 아직 값이 없는 로컬 변수를 읽으려다 에러가 난다. 바깥 변수를 수정하려면 `global num` 선언이 필요하다.

**9. 정답 a) `<class 'tuple'>`**
함수는 언제나 **단 하나의 객체**만 반환한다. 여러 값을 반환하는 것처럼 보여도 실제로는 **하나의 튜플로 자동 패킹**된 것이다.

**10. 정답 c) `TypeError`**
`my_function`은 인자 3개를 요구하는데 리스트 하나만 전달했다. 리스트를 개별 위치 인자로 펼치려면 `my_function(*names)`처럼 **언패킹**해야 한다.

**11. 정답 b) `TypeError`**
`**` 언패킹은 **딕셔너리의 키가 매개변수 이름과 일치할 때만** 동작한다. `nickname`이라는 매개변수는 존재하지 않으므로 "unexpected keyword argument" 에러가 발생한다.

**12. 정답 b) `('서준', 20)`**
`key=lambda s: s[1]`은 튜플의 인덱스 1(나이)을 정렬 기준으로 삼는다. 오름차순 정렬 결과의 첫 요소는 가장 어린 `('서준', 20)`이다.

**13. 정답 c) `3`**
함수를 **정의**할 때 받는 이름(`a`, `b`)은 **매개변수(parameter)**, 함수를 **호출**할 때 넘기는 실제 값(`3`, `5`)이 **인자(argument)**다.

**14. 정답 b) `def f(a=1, b): ...`**
기본값이 있는 매개변수 뒤에 기본값 없는 매개변수가 올 수 없다. 값을 전달하지 않았을 때 `b`에 넣을 값을 결정할 수 없기 때문이다.

**15. 정답 c) `TypeError`**
LEGB 순서상 **Global이 Built-in보다 먼저** 검색되므로, `sum = 10`이 내장 함수 `sum()`을 가려버린다(shadowing). 이후 `sum([1,2,3])`은 정수 `10`을 호출하려는 시도가 되어 "int object is not callable" 에러가 난다. 내장 함수 이름을 변수명으로 쓰지 말아야 하는 이유다.

**16. 정답 d)**
독스트링은 **선택 사항**이다. 없어도 함수는 정상적으로 정의되고 동작한다.

**17. 정답 c)**
`return`문이 없는 함수도 반환값은 존재하며, 그 값이 **`None`**이다. 파이썬 함수는 언제나 `None`을 포함한 단 하나의 객체를 반환한다.

**18. 정답 b) `<class 'tuple'>`**
콤마로 구분된 값들을 한 변수에 넣으면 자동으로 튜플로 **패킹**된다. 소괄호는 생략 가능하다.

**19. 정답 d)**
함수 호출 시 `**딕셔너리`는 딕셔너리를 **개별 키워드 인자**로 펼쳐서 전달한다. 위치 인자 하나로 전달되는 것이 아니다.

**20. 정답 b)**
람다는 **쓰고 바로 버리는 일회성 함수**나, 함수를 인자로 요구하는 자리(`sorted`의 `key`, `map`의 첫 인자 등)에 즉석에서 로직을 넣을 때 적합하다. 복잡하거나 재사용되는 로직은 `def`로 이름 있는 함수를 만드는 것이 낫다.
