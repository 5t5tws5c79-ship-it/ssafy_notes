"""
03. 조건에 맞는 것만 골라내기

> for 문 + if 문의 가장 기본 조합.
>
> 핵심 패턴) 빈 결과 리스트를 만들어 두고, 조건에 맞는 것만 append 한다.
>
>     result = []
>     for n in numbers:
>         if 조건:
>             result.append(n)
>     return result

---

1) evens(numbers)
   짝수만 골라 리스트로 반환한다.

       evens([1, 2, 3, 4, 5, 6])  #=> [2, 4, 6]

   힌트) 짝수는 2로 나눈 나머지가 0. -> n % 2 == 0
         0 도 짝수라는 점에 주의.

2) between(numbers, low, high)
   low **이상** high **이하** 인 값만 골라 반환한다.

       between([1, 5, 10, 15, 20], 5, 15)  #=> [5, 10, 15]

   ⚠️ '이상/이하' 이므로 경계값 5와 15가 포함된다. 등호를 빠뜨리지 말 것.
      파이썬은 low <= n <= high 처럼 이어서 쓸 수 있다.

3) count_sign(numbers)
   양수, 음수, 0 의 개수를 각각 세어 (양수, 음수, 0) 튜플로 반환한다.

       count_sign([1, -2, 0, 5, -7, 0])  #=> (2, 2, 2)

   힌트) 카운터 변수를 3개 만들어 두고 if / elif / else 로 하나씩 올린다.
"""


def evens(numbers):
    result = []

    for n in numbers:
        pass

    return result


def between(numbers, low, high):
    result = []

    for n in numbers:
        # 등호를 빠뜨리면 경계값이 사라진다.
        pass

    return result


def count_sign(numbers):
    positive = 0
    negative = 0
    zero = 0

    for n in numbers:
        # 셋 중 하나에만 해당하므로 if / elif / else 로 쓴다.
        pass

    return positive, negative, zero


if __name__ == '__main__':
    print(evens([1, 2, 3, 4, 5, 6]))   # [2, 4, 6]
    print(evens([1, 3, 5]))            # []
    print(evens([0, -2, -3]))          # [0, -2]

    print(between([1, 5, 10, 15, 20], 5, 15))   # [5, 10, 15]  <- 5와 15 포함!
    print(between([1, 5, 10], 100, 200))        # []

    print(count_sign([1, -2, 0, 5, -7, 0]))   # (2, 2, 2)
    print(count_sign([]))                     # (0, 0, 0)

    # 반환값이 3개처럼 보이지만 실제로는 튜플 하나다. 언패킹해서 받을 수 있다.
    p, n, z = count_sign([1, -2, 0])
    print(f'양수 {p}개, 음수 {n}개, 0 은 {z}개')   # 양수 1개, 음수 1개, 0 은 1개
