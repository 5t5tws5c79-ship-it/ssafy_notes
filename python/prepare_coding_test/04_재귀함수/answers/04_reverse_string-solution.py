"""
04. 문자열 뒤집기 - 풀이
"""


def reverse_string(word):
    # 종료 조건: 빈 문자열은 뒤집어도 빈 문자열입니다.
    if word == '':
        return ''

    # 재귀 호출: 첫 글자를 뗀 나머지를 뒤집고, 그 뒤에 첫 글자를 붙입니다.
    return reverse_string(word[1:]) + word[0]


if __name__ == '__main__':
    print(reverse_string(''))        # ''
    print(reverse_string('a'))       # 'a'
    print(reverse_string('abc'))     # 'cba'
    print(reverse_string('ssafy'))   # 'yfass'

    # 동작 과정
    # reverse_string('abc')
    #   -> reverse_string('bc') + 'a'
    #        -> reverse_string('c') + 'b'
    #             -> reverse_string('') + 'c'
    #                  -> ''            (종료 조건 도달)
    #             -> '' + 'c'  = 'c'
    #        -> 'c' + 'b' = 'cb'
    #   -> 'cb' + 'a' = 'cba'
