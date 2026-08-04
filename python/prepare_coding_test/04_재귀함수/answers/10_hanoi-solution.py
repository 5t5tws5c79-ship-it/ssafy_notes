"""
10. 하노이의 탑 - 풀이
"""


def hanoi(n, start, target, via):
    # 종료 조건: 옮길 원반이 없으면 이동 횟수는 0입니다.
    if n == 0:
        return 0

    # (1) 위쪽 n-1개를 보조 기둥(via)으로 옮깁니다.
    #     이 단계에서는 via가 목표가 되고, target이 경유지가 됩니다.
    count = hanoi(n - 1, start, via, target)

    # (2) 가장 큰 n번 원반을 목표 기둥으로 옮깁니다.
    print(f'{n}번 원반: {start} -> {target}')
    count += 1

    # (3) 보조 기둥에 있던 n-1개를 목표 기둥으로 옮깁니다.
    count += hanoi(n - 1, via, target, start)

    return count


if __name__ == '__main__':
    print(hanoi(1, 'A', 'C', 'B'))  # 1
    print('---')
    print(hanoi(2, 'A', 'C', 'B'))  # 3
    print('---')
    print(hanoi(3, 'A', 'C', 'B'))  # 7

    # 원반이 n개일 때 최소 이동 횟수는 2^n - 1 입니다.
    # 원반 하나가 늘어날 때마다 이동 횟수가 두 배가 되므로,
    # n이 조금만 커져도 출력이 폭발적으로 늘어납니다.
