"""
03. 공백으로 구분된 숫자 문자열 다루기 - 풀이
"""


def even_only(numbers):
    result = []

    # 문자열 -> 리스트 -> 각각 정수로 변환
    for n in map(int, numbers.split()):
        if n % 2 == 0:
            # 다시 문자열로 이어 붙일 것이므로 str() 로 바꿔 담는다.
            result.append(str(n))

    return ' '.join(result)


def top_three(numbers):
    number_list = list(map(int, numbers.split()))

    # 내림차순 정렬 후 앞에서 3개
    number_list.sort(reverse=True)
    top = number_list[:3]

    # join 은 문자열 리스트만 받으므로 map(str, ...) 로 바꿔 넘긴다.
    return ' '.join(map(str, top))


def sum_of_digits(numbers):
    total = 0

    for token in numbers.split():
        # 문자열을 한 글자씩 돌면 각 자릿수가 나온다. '123' -> '1', '2', '3'
        for digit in token:
            total += int(digit)

    return total


if __name__ == '__main__':
    print(repr(even_only('1 2 3 4 5 6')))
    print(repr(even_only('1 3 5')))
    print(repr(even_only('10 7 24')))

    print(repr(top_three('5 1 9 3 7')))
    print(repr(top_three('4 2')))

    print(sum_of_digits('12 34'))
    print(sum_of_digits('1 2 3'))
    print(sum_of_digits('999'))

    # split() 을 괄호 없이 부르면 공백이 몇 칸이든, 앞뒤에 있든 알아서 잘라 준다.
    print('1   2  3'.split())
    print('1   2  3'.split(' '))
