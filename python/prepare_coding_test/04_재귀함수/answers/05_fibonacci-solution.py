"""
05. 피보나치 수열 - 풀이
"""


def fib(n):
    # 종료 조건: 0번째 항은 0, 1번째 항은 1입니다.
    if n < 2:
        return n

    # 재귀 호출: 바로 앞의 두 항을 더합니다.
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(0))   # 0
    print(fib(1))   # 1
    print(fib(7))   # 13
    print(fib(10))  # 55
    print([fib(i) for i in range(11)])
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # 주의) 위 재귀는 같은 계산을 반복해서 호출 횟수가 기하급수적으로 늘어납니다.
    #       fib(35) 정도만 되어도 눈에 띄게 느려집니다.
    #       이미 구한 값을 저장해두면(메모이제이션) 훨씬 빨라집니다.
    def fib_memo(n, memo=None):
        if memo is None:
            memo = {}
        if n < 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]

    print(fib_memo(50))  # 12586269025
