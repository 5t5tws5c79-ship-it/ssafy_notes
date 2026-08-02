"""
02. 최댓값 / 최솟값 직접 찾기

> 내장 함수 max(), min(), sum() 을 쓰지 말고 반복문으로 직접 찾아본다.
>
> 핵심 패턴) "지금까지 가장 큰 값"을 담아둘 변수를 하나 만들고,
>            리스트를 돌면서 더 큰 값을 만나면 바꿔치기한다.

---

1) find_max(numbers)
   가장 큰 값을 반환한다. 빈 리스트면 None.

       find_max([3, 7, 2, 9, 4])  #=> 9

   ⚠️ 시작값을 0 으로 두면 안 된다. 리스트가 전부 음수일 때 0 이 나와버린다.
      **첫 번째 값(numbers[0])을 일단 최댓값이라고 가정하고** 시작할 것.

2) find_min_index(numbers)
   가장 작은 값이 몇 번째에 있는지 그 **인덱스**를 반환한다. 빈 리스트면 -1.
   같은 값이 여러 개면 앞쪽 것.

       find_min_index([3, 7, 2, 9, 4])  #=> 2

   힌트) 값이 아니라 위치가 필요하므로 for i in range(len(numbers)) 로 돈다.

3) total_and_average(numbers)
   합계와 평균을 함께 반환한다. 빈 리스트면 (0, 0).

       total_and_average([1, 2, 3, 4])  #=> (10, 2.5)

   힌트) return 에 값을 콤마로 나열하면 튜플 하나로 묶여서 반환된다.
"""


def find_max(numbers):
    # 빈 리스트면 비교할 대상이 없다.

    # 첫 번째 값을 일단 최댓값이라고 가정하고 시작한다.
    pass


def find_min_index(numbers):
    # 지금까지 가장 작았던 값의 '인덱스'를 담아둔다.
    pass


def total_and_average(numbers):
    # 나누기 전에 빈 리스트를 걸러야 한다. (0으로 나누면 ZeroDivisionError)
    pass


if __name__ == '__main__':
    print(find_max([3, 7, 2, 9, 4]))     # 9
    print(find_max([-5, -1, -8]))        # -1   <- 여기서 0이 나오면 틀린 것
    print(find_max([42]))                # 42
    print(find_max([]))                  # None

    print(find_min_index([3, 7, 2, 9, 4]))   # 2
    print(find_min_index([5, 1, 1, 8]))      # 1   (동점이면 앞쪽)
    print(find_min_index([]))                # -1

    print(total_and_average([1, 2, 3, 4]))   # (10, 2.5)
    print(total_and_average([10]))           # (10, 10.0)
    print(total_and_average([]))             # (0, 0)
