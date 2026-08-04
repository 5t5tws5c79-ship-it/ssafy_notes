"""
03. 리스트 원소의 합 - 풀이
"""


def sum_list(numbers):
    # 종료 조건: 빈 리스트의 합은 0입니다.
    if not numbers:
        return 0

    # 재귀 호출: 첫 원소 + 나머지 리스트(numbers[1:])의 합
    return numbers[0] + sum_list(numbers[1:])


if __name__ == '__main__':
    print(sum_list([]))             # 0
    print(sum_list([7]))            # 7
    print(sum_list([1, 2, 3, 4]))   # 10
    print(sum_list([10, -3, 5]))    # 12

    # 참고) 인덱스를 넘기는 방식 (슬라이싱으로 리스트를 새로 만들지 않아 메모리에 유리)
    def sum_list_idx(numbers, i=0):
        if i == len(numbers):
            return 0
        return numbers[i] + sum_list_idx(numbers, i + 1)

    print(sum_list_idx([1, 2, 3, 4]))  # 10
