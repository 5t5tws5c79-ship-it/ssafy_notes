"""
03. 대댓글 트리 (재귀) - 풀이
"""

# ============================================================================
# 연습용 데이터 (대댓글이 최대 5단까지 중첩된 댓글 트리)
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
# 풀이
# ============================================================================
def count_comments(node):
    # 자기 자신 1개로 시작한다.
    total = 1

    # 종료 조건: replies 가 빈 리스트면 for 문이 한 번도 돌지 않고 1을 반환한다.
    for reply in node['replies']:
        total += count_comments(reply)   # 재귀 호출

    return total


def max_depth(node):
    # 종료 조건: 대댓글이 없으면 자기 자신 한 층뿐이다.
    if not node['replies']:
        return 1

    # 자식들 중 가장 깊은 것을 골라 자기 층(1)을 더한다.
    return 1 + max(max_depth(reply) for reply in node['replies'])

    # 위 한 줄을 풀어 쓰면 아래와 같다.
    # deepest = 0
    # for reply in node['replies']:
    #     deepest = max(deepest, max_depth(reply))
    # return 1 + deepest


def total_likes(node):
    # 자기 좋아요 + 모든 대댓글의 좋아요
    total = node['likes']

    for reply in node['replies']:
        total += total_likes(reply)

    return total


def collect_by_author(node, author):
    result = []

    # 자기 자신부터 확인한다. (위에서 아래로 훑으므로 등장 순서가 유지된다)
    if node['author'] == author:
        result.append(node['text'])

    for reply in node['replies']:
        result += collect_by_author(reply, author)   # 재귀 호출

    return result


def find_by_id(node, target):
    # 종료 조건 1: 찾았다.
    if node['id'] == target:
        return node

    for reply in node['replies']:
        found = find_by_id(reply, target)
        # 자식 쪽에서 찾았다면 더 뒤질 필요 없이 바로 올려보낸다.
        if found is not None:
            return found

    # 종료 조건 2: 이 가지에는 없다.
    return None


if __name__ == '__main__':
    print('--- 1) 전체 댓글 수 ---')
    print(count_comments(THREAD))

    print('--- 2) 최대 깊이 ---')
    print(max_depth(THREAD))

    print('--- 3) 좋아요 합계 ---')
    print(total_likes(THREAD))

    print('--- 4) 작성자별 댓글 모으기 ---')
    for author in ('gildong', 'ssafy_kim', 'newbie', 'nobody'):
        print(author, collect_by_author(THREAD, author))

    print('--- 5) id 로 댓글 찾기 (보너스) ---')
    print(find_by_id(THREAD, 5)['text'])
    print(find_by_id(THREAD, 999))

    print('--- 보너스) 트리 모양으로 출력하기 ---')

    def print_tree(node, depth=0):
        print('  ' * depth + f"└ {node['author']}: {node['text']} (♥{node['likes']})")
        for reply in node['replies']:
            print_tree(reply, depth + 1)

    print_tree(THREAD)
