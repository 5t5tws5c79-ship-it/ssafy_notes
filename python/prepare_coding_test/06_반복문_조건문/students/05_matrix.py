"""
05. 중첩 반복문 - 2차원 리스트

> 리스트 안에 리스트가 들어 있는 구조.
>
>     matrix = [
>         [1, 2, 3],     <- matrix[0]
>         [4, 5, 6],     <- matrix[1]
>         [7, 8, 9],     <- matrix[2]
>     ]
>
>     matrix[1]      #=> [4, 5, 6]   (행 하나가 통째로 나온다)
>     matrix[1][2]   #=> 6           (1번 행의 2번 칸)
>
> 한 겹만 돌면 '행'이 나오고, 두 겹을 돌아야 '숫자'에 닿는다.
>
>     for row in matrix:        # row 는 리스트
>         for value in row:     # value 가 비로소 숫자
>             ...

---

1) row_sums(matrix)
   각 행의 합계를 리스트로 반환한다.

       row_sums([[1,2,3], [4,5,6], [7,8,9]])  #=> [6, 15, 24]

2) count_greater(matrix, n)
   전체에서 n 보다 큰 값이 몇 개인지 센다.

       count_greater(matrix, 5)  #=> 4   (6, 7, 8, 9)

3) find_position(matrix, target)
   target 이 있는 위치를 (행 번호, 열 번호) 로 반환한다. 없으면 (-1, -1).

       find_position(matrix, 5)   #=> (1, 1)
       find_position(matrix, 99)  #=> (-1, -1)

   힌트) 위치가 필요하므로 값이 아니라 인덱스로 돌아야 한다.

           for i in range(len(matrix)):
               for j in range(len(matrix[i])):
                   matrix[i][j] ...
"""


def row_sums(matrix):
    result = []

    # 바깥 for 는 행(리스트)을, 안쪽 for 는 그 행의 숫자를 꺼낸다.
    for row in matrix:
        pass

    return result


def count_greater(matrix, n):
    count = 0

    for row in matrix:
        pass

    return count


def find_position(matrix, target):
    # 값이 아니라 위치가 필요하므로 range(len(...)) 로 인덱스를 돈다.
    pass


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(row_sums(matrix))          # [6, 15, 24]
    print(row_sums([[10], [20]]))    # [10, 20]
    print(row_sums([]))              # []

    print(count_greater(matrix, 5))   # 4
    print(count_greater(matrix, 0))   # 9
    print(count_greater(matrix, 99))  # 0

    print(find_position(matrix, 5))   # (1, 1)
    print(find_position(matrix, 1))   # (0, 0)
    print(find_position(matrix, 99))  # (-1, -1)

    # ------------------------------------------------------------------
    # ⚠️ 2차원 리스트를 직접 만들어야 할 때 절대 하면 안 되는 것
    bad = [[0] * 3] * 3
    bad[0][0] = 9
    print(bad)    # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  <- 세 행이 같이 바뀐다!

    good = [[0] * 3 for _ in range(3)]
    good[0][0] = 9
    print(good)   # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]  <- 이게 정상
