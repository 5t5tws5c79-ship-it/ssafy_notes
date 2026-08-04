"""
04. break / continue / while

> 반복을 중간에 제어하는 방법.
>
>     break    : 반복문 자체를 즉시 끝낸다. 뒤에 남은 것은 아예 보지 않는다.
>     continue : 이번 것만 건너뛰고 다음 반복으로 넘어간다. 반복은 계속된다.
>
> 이 둘의 차이가 이 문제의 핵심이다.

---

1) first_negative(numbers)
   처음으로 나온 음수를 반환한다. 음수가 없으면 None.

       first_negative([3, 5, -2, 7, -9])  #=> -2

   힌트) 찾자마자 return 하면 된다. return 은 함수를 즉시 끝내므로
         break 를 따로 쓰지 않아도 반복이 멈춘다.

2) sum_until_zero(numbers)
   앞에서부터 더하다가 **0 을 만나면 멈춘다.** 0 과 그 뒤는 더하지 않는다.

       sum_until_zero([1, 2, 3, 0, 100])  #=> 6

   힌트) break

3) sum_skip_multiples_of_3(numbers)
   3의 배수만 **빼고** 전부 더한다.

       sum_skip_multiples_of_3([1, 2, 3, 4, 5, 6])  #=> 12

   힌트) continue

4) countdown(n)
   n 부터 1 까지 거꾸로 담은 리스트를 반환한다. **while 문으로** 작성할 것.

       countdown(5)  #=> [5, 4, 3, 2, 1]

   ⚠️ while 안에서 n 을 줄이지 않으면 무한 루프가 된다. 반드시 종료를 향해 가야 한다.
"""


def first_negative(numbers):
    for n in numbers:
        pass

    # 끝까지 돌았는데 못 찾았다는 뜻
    return None


def sum_until_zero(numbers):
    total = 0

    for n in numbers:
        # 0을 만나면 반복 자체를 끝낸다.
        pass

    return total


def sum_skip_multiples_of_3(numbers):
    total = 0

    for n in numbers:
        # 3의 배수면 이번 것만 건너뛴다.
        pass

    return total


def countdown(n):
    result = []

    # while 문으로 직접 작성한다.
    #   while 조건:
    #       result 에 담고
    #       n 을 줄인다
    # ⚠️ n 을 줄이는 줄을 빼먹으면 프로그램이 멈추지 않는다. (무한 루프)

    return result


if __name__ == '__main__':
    print(first_negative([3, 5, -2, 7, -9]))   # -2   (뒤의 -9가 아니라 처음 만난 것)
    print(first_negative([1, 2, 3]))           # None
    print(first_negative([]))                  # None

    print(sum_until_zero([1, 2, 3, 0, 100]))   # 6    (0 뒤의 100은 안 더해짐)
    print(sum_until_zero([1, 2, 3]))           # 6
    print(sum_until_zero([0, 5]))              # 0

    print(sum_skip_multiples_of_3([1, 2, 3, 4, 5, 6]))   # 12   (3과 6을 건너뜀)
    print(sum_skip_multiples_of_3([3, 6, 9]))            # 0

    print(countdown(5))    # [5, 4, 3, 2, 1]
    print(countdown(1))    # [1]
    print(countdown(0))    # []

    # 참고) break 와 continue 의 차이를 눈으로 확인해 보자.
    for i in range(6):
        if i == 3:
            break
        print(i, end=' ')      # 0 1 2
    print()

    for i in range(6):
        if i == 3:
            continue
        print(i, end=' ')      # 0 1 2 4 5
    print()
