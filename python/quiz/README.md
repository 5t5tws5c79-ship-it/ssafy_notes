# Python 평가 대비 문제집 (총 180문제)

각 노트별로 20문제씩. 문제는 상단, **정답과 해설은 각 파일 최하단**에 있습니다.
사지선다(a~d)이며, 단순 암기보다 **실행 결과 예측·함정 구분·옳지 않은 것 찾기** 위주로 구성했습니다.

| # | 문제 파일 | 원본 노트 | 핵심 출제 포인트 |
|:--:|---|---|---|
| 01 | [파이썬 기초](01_python_basic_quiz.md) | [01_python_basic.md](../01_python_basic.md) | 연산자 우선순위, 단일 요소 튜플, range step 음수, 단축 평가 반환값, `==` vs `is`, 얕은 참조, 부동소수점 |
| 02 | [함수](02_python_functions_quiz.md) | [02_python_functions.md](../02_python_functions.md) | 인자 5종 순서, `*args`/`**kwargs`, LEGB, `UnboundLocalError`, shadowing, 패킹/언패킹 |
| 03 | [모듈 & 패키지](03_python_modules_quiz.md) | [03_python_modules.md](../03_python_modules.md) | import 방식 비교, 이름 충돌, `as`, PSL vs 외부 패키지, pip/requirements |
| 04 | [제어문](04_control_of_flow_quiz.md) | [04_control_of_flow.md](../04_control_of_flow.md) | 조건문 순서 함정, for-else, enumerate, zip 절삭, `zip(*matrix)`, map 다중 iterable |
| 05 | [데이터 구조 1](05_data_structure_quiz.md) | [05_data_structure.md](../05_data_structure.md) | append vs extend, `insert(-1)`, pop 반환, sort는 None 반환, 얕은/깊은 복사, `[[0]*5]*5` |
| 06 | [데이터 구조 2](06_data_structure_2_quiz.md) | [06_data_structure_2.md](../06_data_structure_2.md) | get/setdefault/popitem, defaultdict 키 생성, add vs update, remove vs discard, 해시 가능성 |
| 07 | [OOP 1](07_oop_01_quiz.md) | [07_oop_01.md](../07_oop_01.md) | 클래스 변수 대입 함정, self 동작 원리, 메서드 3종, 네임스페이스 탐색, 매직 메서드, 데코레이터 |
| 08 | [OOP 2 (상속)](08_oop_02_quiz.md) | [08_oop_02.md](../08_oop_02.md) | 오버라이딩/오버로딩, 다중 상속 순서, MRO(C3), `super()`는 부모가 아닌 MRO 다음, 협력적 다중 상속 |
| 09 | [예외 처리](09_exception_handling_quiz.md) | [09_exception_handling.md](../09_exception_handling.md) | SyntaxError vs Exception, 예외별 발생 상황, except 순서, else/finally, EAFP vs LBYL |

---

## 특히 자주 틀리는 함정 모음

- `-2 ** 4` → `-16` (거듭제곱이 단항 부호보다 우선)
- `(1)`은 `int`, `(1,)`이 `tuple`
- `and`/`or`는 `True`/`False`가 아니라 **피연산자 값 자체**를 반환
- `append([3,4])`는 `[1,2,[3,4]]`, `extend([3,4])`가 `[1,2,3,4]`
- `L = L.sort()` → `L`은 `None` (원본 수정 + 반환값 없음)
- `L.insert(-1, x)`는 맨 끝이 아니라 **마지막 요소 바로 앞**
- 얕은 복사(`a[:]`)는 중첩 객체를 공유 → `a[2] is b[2]`가 `True`
- `defaultdict`는 `d[key]` 조회만으로 키가 생성됨 (`get()`, `in`은 생성 안 함)
- 딕셔너리 `pop()`은 키 인자 필수 (리스트와 다름)
- 세트 `add('abc')` → `{'abc'}` / `update('abc')` → `{'a','b','c'}`
- `c1.pi = 100`은 클래스 변수 수정이 아니라 **인스턴스 변수 신규 생성**
- `super()`는 "부모"가 아니라 **"MRO상 나의 다음 클래스"**
- `except Exception`을 위에 두면 아래 구체적 예외는 절대 도달 못 함
