"""
03. 리스트 원소의 합

> 숫자로 이루어진 리스트 numbers를 입력받아 모든 원소의 합을 반환하는 함수를 재귀로 작성하시오.
> (내장 함수 sum() 은 사용하지 않는다.)
>
> 힌트) numbers[0] + (나머지 리스트의 합) 으로 쪼갤 수 있다. 나머지 리스트는 numbers[1:]

예시)
    sum_list([])           #=> 0
    sum_list([1, 2, 3])    #=> 6
    sum_list([10, -3, 5])  #=> 12
"""


def sum_list(numbers):
    # 종료 조건: 빈 리스트의 합은 0입니다.

    # 재귀 호출: 첫 원소 + 나머지 리스트의 합
    pass


if __name__ == '__main__':
    print(sum_list([]))             # 0
    print(sum_list([7]))            # 7
    print(sum_list([1, 2, 3, 4]))   # 10
    print(sum_list([10, -3, 5]))    # 12
