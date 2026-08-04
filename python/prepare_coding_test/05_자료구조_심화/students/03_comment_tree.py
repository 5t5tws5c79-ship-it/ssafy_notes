"""
03. 대댓글 트리 (재귀)

> THREAD 는 대댓글이 몇 겹까지 중첩될지 알 수 없는 댓글 트리이다.
> 모든 댓글은 아래와 같은 모양이고, replies 안에 다시 같은 모양의 댓글들이 들어 있다.
>
>     {
>         'id': 1,
>         'author': 'gildong',
>         'text': '재귀 함수 언제 쓰는 건가요?',
>         'likes': 12,
>         'replies': [ {...}, {...} ],   # <- 여기 또 같은 모양의 댓글!
>     }
>
> 깊이를 미리 알 수 없으므로 for 문을 몇 번 겹쳐 쓸지 정할 수 없다.
> 이런 구조가 바로 재귀를 써야 하는 대표적인 경우다.
>
> 공통 힌트) "댓글 하나를 처리한다" = "자기 자신을 처리 + 각 replies 를 같은 방식으로 처리"
>            종료 조건은 replies 가 빈 리스트일 때 자연스럽게 만들어진다.

---

1) count_comments(node)   : 자기 자신을 포함한 전체 댓글 개수
2) max_depth(node)        : 가장 깊은 곳까지의 층수 (루트 혼자면 1)
3) total_likes(node)      : 트리 전체의 좋아요 합계
4) collect_by_author(node, author) : 특정 작성자가 쓴 댓글의 text 를 위에서부터 순서대로 모은 리스트
"""

# ============================================================================
# 연습용 데이터 (대댓글이 최대 5단까지 중첩된 댓글 트리)
# 읽고 넘어가면 된다. 문제는 아래 함수부터.
# ============================================================================
THREAD = {
    'id': 1,
    'author': 'gildong',
    'text': '재귀 함수 언제 쓰는 건가요?',
    'likes': 12,
    'replies': [
        {
            'id': 2,
            'author': 'ssafy_kim',
            'text': '트리처럼 깊이를 모르는 구조를 다룰 때 편합니다.',
            'likes': 30,
            'replies': [
                {
                    'id': 3,
                    'author': 'gildong',
                    'text': '깊이를 모른다는 게 무슨 뜻인가요?',
                    'likes': 4,
                    'replies': [
                        {
                            'id': 4,
                            'author': 'ssafy_kim',
                            'text': '지금 이 댓글창처럼 대댓글이 몇 단까지 달릴지 모르는 경우요.',
                            'likes': 25,
                            'replies': [
                                {
                                    'id': 5,
                                    'author': 'newbie',
                                    'text': '아 이해했습니다!',
                                    'likes': 3,
                                    'replies': [],
                                },
                            ],
                        },
                    ],
                },
                {
                    'id': 6,
                    'author': 'park',
                    'text': '반복문으로도 되긴 하는데 코드가 길어져요.',
                    'likes': 8,
                    'replies': [],
                },
            ],
        },
        {
            'id': 7,
            'author': 'newbie',
            'text': '스택 오버플로가 뭔가요?',
            'likes': 1,
            'replies': [
                {
                    'id': 8,
                    'author': 'park',
                    'text': '종료 조건에 못 닿으면 호출이 끝없이 쌓여서 터지는 겁니다.',
                    'likes': 17,
                    'replies': [],
                },
            ],
        },
        {
            'id': 9,
            'author': 'gildong',
            'text': '정리 감사합니다.',
            'likes': 5,
            'replies': [],
        },
    ],
}


# ============================================================================
# 여기부터 문제
# ============================================================================
def count_comments(node):
    # 자기 자신 1개로 시작해서, 각 대댓글의 개수를 더해 나간다.
    total = 1

    for reply in node['replies']:
        # 재귀 호출
        pass

    return total


def max_depth(node):
    # 종료 조건: 대댓글이 없으면 자기 한 층뿐이다.

    # 재귀 호출: 자식들 중 가장 깊은 값에 자기 층(1)을 더한다.
    #            힌트) max() 를 활용
    pass


def total_likes(node):
    # count_comments 와 구조가 똑같다. 시작값만 다르다.
    pass


def collect_by_author(node, author):
    result = []

    # 1) 자기 자신이 그 작성자면 text 를 담는다.
    # 2) 각 대댓글에서 모은 결과를 이어 붙인다. (리스트끼리는 += 로 이어 붙일 수 있다)

    return result


if __name__ == '__main__':
    print('--- 1) 전체 댓글 수 ---')
    print(count_comments(THREAD))   # 9

    print('--- 2) 최대 깊이 ---')
    print(max_depth(THREAD))        # 5

    print('--- 3) 좋아요 합계 ---')
    print(total_likes(THREAD))      # 105

    print('--- 4) 작성자별 댓글 모으기 ---')
    for author in ('gildong', 'ssafy_kim', 'newbie', 'nobody'):
        print(author, collect_by_author(THREAD, author))
    # gildong   ['재귀 함수 언제 쓰는 건가요?', '깊이를 모른다는 게 무슨 뜻인가요?', '정리 감사합니다.']
    # ssafy_kim ['트리처럼 깊이를 모르는 구조를 다룰 때 편합니다.', '지금 이 댓글창처럼 ...']
    # newbie    ['아 이해했습니다!', '스택 오버플로가 뭔가요?']
    # nobody    []

    # 도전) 아래처럼 트리 모양 그대로 출력하는 print_tree(node, depth=0) 도 만들어 보시오.
    # └ gildong: 재귀 함수 언제 쓰는 건가요? (♥12)
    #   └ ssafy_kim: 트리처럼 깊이를 모르는 구조를 다룰 때 편합니다. (♥30)
    #     └ gildong: 깊이를 모른다는 게 무슨 뜻인가요? (♥4)
    #       ...
