"""
05. 중첩 반복문 - 2차원 리스트 - 풀이
"""


def row_sums(matrix):
    result = []

    # 바깥 for: 행(row)을 하나씩 꺼낸다. row 는 리스트다.
    for row in matrix:
        total = 0
        # 안쪽 for: 그 행의 숫자를 하나씩 꺼낸다.
        for value in row:
            total += value
        result.append(total)

    return result


def count_greater(matrix, n):
    count = 0

    for row in matrix:
        for value in row:
            if value > n:
                count += 1

    return count


def find_position(matrix, target):
    # 위치(행 번호, 열 번호)가 필요하므로 range(len(...)) 로 인덱스를 돈다.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return i, j

    return -1, -1


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(row_sums(matrix))          # [6, 15, 24]
    print(row_sums([[10], [20]]))    # [10, 20]
    print(row_sums([]))              # []

    print(count_greater(matrix, 5))  # 4   (6, 7, 8, 9)
    print(count_greater(matrix, 0))  # 9
    print(count_greater(matrix, 99)) # 0

    print(find_position(matrix, 5))   # (1, 1)
    print(find_position(matrix, 1))   # (0, 0)
    print(find_position(matrix, 99))  # (-1, -1)

    # ------------------------------------------------------------------
    # ⚠️ 2차원 리스트를 만들 때 절대 하면 안 되는 것
    bad = [[0] * 3] * 3
    bad[0][0] = 9
    print(bad)    # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  <- 세 행이 같이 바뀜!

    good = [[0] * 3 for _ in range(3)]
    good[0][0] = 9
    print(good)   # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]  <- 이게 정상

    # 이유) [x] * 3 은 x 를 3번 '복사'하는 게 아니라 같은 것을 3번 '가리킨다'.
    #       안쪽이 리스트면 세 행이 전부 같은 리스트가 되어버린다.
