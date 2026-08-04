"""
02. 최댓값 / 최솟값 직접 찾기 - 풀이
"""


def find_max(numbers):
    # 빈 리스트면 비교할 대상이 없다.
    if not numbers:
        return None

    # 첫 번째 값을 일단 최댓값이라고 가정하고 시작한다.
    # (0 으로 시작하면 전부 음수인 리스트에서 틀린다!)
    biggest = numbers[0]

    for n in numbers:
        if n > biggest:
            biggest = n

    return biggest


def find_min_index(numbers):
    if not numbers:
        return -1

    smallest_index = 0

    # 값이 아니라 '인덱스'가 필요하므로 range(len(...)) 로 순회한다.
    for i in range(len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i

    return smallest_index


def total_and_average(numbers):
    if not numbers:
        return 0, 0

    total = 0

    for n in numbers:
        total += n

    return total, total / len(numbers)


if __name__ == '__main__':
    print(find_max([3, 7, 2, 9, 4]))     # 9
    print(find_max([-5, -1, -8]))        # -1
    print(find_max([42]))                # 42
    print(find_max([]))                  # None

    print(find_min_index([3, 7, 2, 9, 4]))   # 2
    print(find_min_index([5, 1, 1, 8]))      # 1  (동점이면 앞쪽)
    print(find_min_index([]))                # -1

    print(total_and_average([1, 2, 3, 4]))   # (10, 2.5)
    print(total_and_average([10]))           # (10, 10.0)
    print(total_and_average([]))             # (0, 0)

    # ------------------------------------------------------------------
    # 흔한 오답: 0 으로 시작하면 전부 음수일 때 0 이 나와버린다.
    def wrong_max(numbers):
        biggest = 0
        for n in numbers:
            if n > biggest:
                biggest = n
        return biggest

    print(wrong_max([-5, -1, -8]))   # 0  <- 리스트에 없는 값이 나옴
