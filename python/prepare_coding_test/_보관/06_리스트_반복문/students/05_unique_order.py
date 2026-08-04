"""
05. 순서를 지키는 중복 제거 / 교집합

> set 을 쓰면 중복 제거와 교집합을 한 줄로 할 수 있지만, **순서가 보장되지 않는다.**
>
>     set([3, 1, 4, 1, 5])            #=> {1, 3, 4, 5}   (넣은 순서가 사라짐)
>     set([3, 1]) & set([1, 5])       #=> {1}
>
> 이 문제에서는 set 을 쓰지 말고, for 문과 리스트만으로 **처음 나온 순서를 지키면서**
> 결과를 만들어 보시오.
>
> 핵심 패턴) 결과 리스트를 하나 만들어 두고,
>            "아직 결과에 없으면(not in) 담는다" 를 반복하면 중복 없이 순서가 지켜진다.

---

1) unique(numbers)
   중복을 제거하되 처음 나온 순서를 유지한다.

       unique([3, 1, 3, 2, 1, 5])  #=> [3, 1, 2, 5]

2) common(a, b)
   두 리스트에 모두 들어 있는 값을 a 의 순서대로, 중복 없이 반환한다.

       common([3, 1, 4, 1, 5], [1, 5, 9, 1])  #=> [1, 5]

3) only_in_a(a, b)
   a 에만 있고 b 에는 없는 값을 a 의 순서대로, 중복 없이 반환한다.

       only_in_a([3, 1, 4, 1, 5], [1, 5, 9])  #=> [3, 4]
"""


def unique(numbers):
    result = []

    for n in numbers:
        # 아직 result 에 없으면 담는다.
        pass

    return result


def common(a, b):
    result = []

    for n in a:
        # b 에도 있고(and) 아직 result 에 없으면 담는다.
        pass

    return result


def only_in_a(a, b):
    result = []

    for n in a:
        # b 에는 없고 아직 result 에도 없으면 담는다.
        pass

    return result


if __name__ == '__main__':
    print(unique([3, 1, 3, 2, 1, 5]))          # [3, 1, 2, 5]
    print(unique(['a', 'b', 'a']))             # ['a', 'b']
    print(unique([]))                          # []

    print(common([3, 1, 4, 1, 5], [1, 5, 9, 1]))   # [1, 5]
    print(common([1, 2], [3, 4]))                  # []

    print(only_in_a([3, 1, 4, 1, 5], [1, 5, 9]))   # [3, 4]
