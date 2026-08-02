"""
04. break / continue / while - 풀이
"""


def first_negative(numbers):
    for n in numbers:
        if n < 0:
            # 찾았으면 더 볼 필요가 없다. return 은 함수를 즉시 끝내므로
            # break 를 따로 쓰지 않아도 반복이 멈춘다.
            return n

    # 끝까지 돌았는데 못 찾았다는 뜻
    return None


def sum_until_zero(numbers):
    total = 0

    for n in numbers:
        if n == 0:
            break          # 0을 만나면 반복 자체를 끝낸다 (뒤는 아예 안 봄)
        total += n

    return total


def sum_skip_multiples_of_3(numbers):
    total = 0

    for n in numbers:
        if n % 3 == 0:
            continue       # 이번 것만 건너뛰고 다음 반복으로 (반복은 계속됨)
        total += n

    return total


def countdown(n):
    result = []

    # while 은 조건이 True 인 동안 계속 돈다.
    # 안에서 n 을 줄이지 않으면 무한 루프가 되니 주의!
    while n > 0:
        result.append(n)
        n -= 1

    return result


if __name__ == '__main__':
    print(first_negative([3, 5, -2, 7, -9]))   # -2  (처음 만난 음수)
    print(first_negative([1, 2, 3]))           # None
    print(first_negative([]))                  # None

    print(sum_until_zero([1, 2, 3, 0, 100]))   # 6    (0 뒤의 100은 안 더해짐)
    print(sum_until_zero([1, 2, 3]))           # 6
    print(sum_until_zero([0, 5]))              # 0

    print(sum_skip_multiples_of_3([1, 2, 3, 4, 5, 6]))   # 12  (3과 6을 건너뜀)
    print(sum_skip_multiples_of_3([3, 6, 9]))            # 0

    print(countdown(5))    # [5, 4, 3, 2, 1]
    print(countdown(1))    # [1]
    print(countdown(0))    # []

    # ------------------------------------------------------------------
    # break 와 continue 의 차이를 한눈에
    print('--- break: 3에서 반복이 끝남 ---')
    for i in range(6):
        if i == 3:
            break
        print(i, end=' ')      # 0 1 2
    print()

    print('--- continue: 3만 건너뛰고 계속 ---')
    for i in range(6):
        if i == 3:
            continue
        print(i, end=' ')      # 0 1 2 4 5
    print()
