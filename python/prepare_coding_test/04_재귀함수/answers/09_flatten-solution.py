"""
09. 중첩 리스트 평탄화 - 풀이
"""


def flatten(nested):
    result = []

    for item in nested:
        # 원소가 리스트라면 그 안을 다시 펼쳐서(재귀 호출) 이어 붙입니다.
        if isinstance(item, list):
            result += flatten(item)
        # 리스트가 아니면 더 쪼갤 것이 없으므로 그대로 담습니다. (종료 조건 역할)
        else:
            result.append(item)

    return result


if __name__ == '__main__':
    print(flatten([1, 2, 3]))              # [1, 2, 3]
    print(flatten([1, [2, 3], 4]))         # [1, 2, 3, 4]
    print(flatten([1, [2, [3, [4]]], 5]))  # [1, 2, 3, 4, 5]
    print(flatten([[], [1], [[2], [3]]]))  # [1, 2, 3]

    # 이 문제의 종료 조건은 "빈 리스트를 만나면 for문이 한 번도 돌지 않고
    # 빈 result를 반환한다"는 점에 숨어 있습니다.
