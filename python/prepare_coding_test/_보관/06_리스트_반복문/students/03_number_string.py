"""
03. 공백으로 구분된 숫자 문자열 다루기

> '1 2 3 4 5' 처럼 공백으로 구분된 숫자 문자열이 주어진다.
> 문자열 -> 리스트 -> 처리 -> 다시 문자열 의 흐름을 연습한다.
>
>     '1 2 3'.split()          #=> ['1', '2', '3']      문자열을 리스트로
>     list(map(int, ['1','2'])) #=> [1, 2]              각 원소를 정수로
>     ' '.join(['1', '2'])     #=> '1 2'                리스트를 문자열로
>
> ⚠️ join 은 **문자열 리스트만** 받는다. 숫자가 들어 있으면 TypeError 가 난다.
>    담을 때 str() 로 바꾸거나, 넘길 때 map(str, ...) 를 쓸 것.

---

1) even_only(numbers)
   짝수만 골라 공백으로 이어 붙인 문자열을 반환한다.

       even_only('1 2 3 4 5 6')  #=> '2 4 6'
       even_only('1 3 5')        #=> ''

2) top_three(numbers)
   가장 큰 수 3개를 큰 순서대로 공백으로 이어 붙여 반환한다.
   3개보다 적게 주어지면 있는 만큼만 반환한다.

       top_three('5 1 9 3 7')  #=> '9 7 5'
       top_three('4 2')        #=> '4 2'

   힌트) 리스트.sort(reverse=True) 로 내림차순 정렬, 슬라이싱 [:3] 으로 앞 3개

3) sum_of_digits(numbers)
   모든 수의 **자릿수**를 전부 더한 값을 정수로 반환한다.

       sum_of_digits('12 34')  #=> 10   (1+2+3+4)
       sum_of_digits('999')    #=> 27

   힌트) 자른 토큰 '12' 를 다시 for 로 돌리면 '1', '2' 가 한 글자씩 나온다.
"""


def even_only(numbers):
    result = []

    # map(int, ...) 는 리스트의 원소를 전부 정수로 바꿔 준다.
    for n in map(int, numbers.split()):
        pass

    return ' '.join(result)


def top_three(numbers):
    number_list = list(map(int, numbers.split()))

    # 내림차순 정렬 -> 앞 3개 -> 문자열로 이어 붙이기
    pass


def sum_of_digits(numbers):
    total = 0

    for token in numbers.split():
        # token 은 '12' 같은 문자열. 이걸 또 한 글자씩 돌린다. (이중 for 문)
        pass

    return total


if __name__ == '__main__':
    print(repr(even_only('1 2 3 4 5 6')))   # '2 4 6'
    print(repr(even_only('1 3 5')))         # ''
    print(repr(even_only('10 7 24')))       # '10 24'

    print(repr(top_three('5 1 9 3 7')))     # '9 7 5'
    print(repr(top_three('4 2')))           # '4 2'

    print(sum_of_digits('12 34'))           # 10
    print(sum_of_digits('1 2 3'))           # 6
    print(sum_of_digits('999'))             # 27
