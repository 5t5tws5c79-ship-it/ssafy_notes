"""
09. 중첩 리스트 평탄화

> 리스트 안에 리스트가 몇 겹으로 들어 있을지 모르는 중첩 리스트를 입력받아,
> 모든 값을 한 줄로 펼친 1차원 리스트를 반환하는 함수를 재귀로 작성하시오.
>
> 힌트) 원소가 리스트인지 확인할 때는 isinstance(item, list) 를 사용한다.

예시)
    flatten([1, [2, 3], 4])            #=> [1, 2, 3, 4]
    flatten([1, [2, [3, [4]]], 5])     #=> [1, 2, 3, 4, 5]
"""


def flatten(nested):
    result = []

    for item in nested:
        # 원소가 리스트라면? -> 그 안을 다시 flatten 해서 이어 붙입니다. (재귀 호출)

        # 원소가 리스트가 아니라면? -> 그냥 result에 담습니다. (종료 조건 역할)
        pass

    return result


if __name__ == '__main__':
    print(flatten([1, 2, 3]))              # [1, 2, 3]
    print(flatten([1, [2, 3], 4]))         # [1, 2, 3, 4]
    print(flatten([1, [2, [3, [4]]], 5]))  # [1, 2, 3, 4, 5]
    print(flatten([[], [1], [[2], [3]]]))  # [1, 2, 3]
