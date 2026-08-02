"""
04. 문자열 뒤집기

> 문자열 word를 입력받아 거꾸로 뒤집은 문자열을 반환하는 함수를 재귀로 작성하시오.
> (슬라이싱 word[::-1] 이나 reversed() 는 사용하지 않는다.)
>
> 힌트) 'abc' -> reverse('bc') + 'a' -> 'cb' + 'a' -> 'cba'

예시)
    reverse_string('')       #=> ''
    reverse_string('abc')    #=> 'cba'
    reverse_string('ssafy')  #=> 'yfass'
"""


def reverse_string(word):
    # 종료 조건: 빈 문자열은 뒤집어도 빈 문자열입니다.

    # 재귀 호출: 첫 글자를 떼고 뒤집은 뒤, 맨 뒤에 첫 글자를 붙입니다.
    pass


if __name__ == '__main__':
    print(reverse_string(''))        # ''
    print(reverse_string('a'))       # 'a'
    print(reverse_string('abc'))     # 'cba'
    print(reverse_string('ssafy'))   # 'yfass'
