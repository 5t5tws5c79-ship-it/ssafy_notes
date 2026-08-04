"""
02. 게시글 / 댓글 집계 - 풀이
"""

# ============================================================================
# 연습용 데이터 (jsonplaceholder.typicode.com 의 실제 응답에서 추린 것)
# ============================================================================
USERS = [
    {'id': 1, 'name': 'Leanne Graham'},
    {'id': 2, 'name': 'Ervin Howell'},
    {'id': 3, 'name': 'Clementine Bauch'},
    {'id': 4, 'name': 'Patricia Lebsack'},
    {'id': 5, 'name': 'Chelsey Dietrich'},
    {'id': 6, 'name': 'Mrs. Dennis Schulist'},
    {'id': 7, 'name': 'Kurtis Weissnat'},
    {'id': 8, 'name': 'Nicholas Runolfsdottir V'},
    {'id': 9, 'name': 'Glenna Reichert'},
    {'id': 10, 'name': 'Clementina DuBuque'},
]

POSTS = [
    {'id': 1, 'userId': 1, 'title': 'sunt aut facere repellat provident occaecati'},
    {'id': 8, 'userId': 1, 'title': 'dolorem dolore est ipsam'},
    {'id': 15, 'userId': 2, 'title': 'eveniet quod temporibus'},
    {'id': 22, 'userId': 3, 'title': 'dolor sint quo a velit explicabo quia nam'},
    {'id': 29, 'userId': 3, 'title': 'iusto eius quod necessitatibus culpa ea'},
    {'id': 36, 'userId': 4, 'title': 'fuga nam accusamus voluptas reiciendis itaque'},
    {'id': 43, 'userId': 5, 'title': 'eligendi iste nostrum consequuntur adipisci'},
    {'id': 50, 'userId': 5, 'title': 'repellendus qui recusandae incidunt voluptates'},
    {'id': 57, 'userId': 6, 'title': 'sed ab est est'},
    {'id': 64, 'userId': 7, 'title': 'et fugit quas eum in in aperiam quod'},
    {'id': 71, 'userId': 8, 'title': 'et iusto veniam et illum aut fuga'},
    {'id': 78, 'userId': 8, 'title': 'quam voluptatibus rerum veritatis'},
    {'id': 85, 'userId': 9, 'title': 'dolore veritatis porro provident adipisci'},
    {'id': 92, 'userId': 10, 'title': 'ratione ex tenetur perferendis'},
    {'id': 99, 'userId': 10, 'title': 'temporibus sit alias delectus eligendi possimus'},
]

COMMENTS = [
    {'id': 1, 'postId': 1, 'email': 'Eliseo@gardner.biz'},
    {'id': 2, 'postId': 1, 'email': 'Jayne_Kuhic@sydney.com'},
    {'id': 3, 'postId': 1, 'email': 'Nikita@garfield.biz'},
    {'id': 4, 'postId': 1, 'email': 'Lew@alysha.tv'},
    {'id': 36, 'postId': 8, 'email': 'Raheem_Heaney@gretchen.biz'},
    {'id': 37, 'postId': 8, 'email': 'Jacky@victoria.net'},
    {'id': 38, 'postId': 8, 'email': 'Piper@linwood.us'},
    {'id': 39, 'postId': 8, 'email': 'Gaylord@russell.net'},
    {'id': 40, 'postId': 8, 'email': 'Clare.Aufderhar@nicole.ca'},
    {'id': 71, 'postId': 15, 'email': 'Lavinia@lafayette.me'},
    {'id': 106, 'postId': 22, 'email': 'Allen@richard.biz'},
    {'id': 107, 'postId': 22, 'email': 'Nicholaus@mikayla.ca'},
    {'id': 141, 'postId': 29, 'email': 'Ottis@lourdes.org'},
    {'id': 142, 'postId': 29, 'email': 'Estel@newton.ca'},
    {'id': 143, 'postId': 29, 'email': 'Bertha@erik.co.uk'},
    {'id': 176, 'postId': 36, 'email': 'Esther@ford.me'},
    {'id': 177, 'postId': 36, 'email': 'Naomie_Cronin@rick.co.uk'},
    {'id': 178, 'postId': 36, 'email': 'Darryl@reginald.us'},
    {'id': 179, 'postId': 36, 'email': 'Thea@aurelio.org'},
    {'id': 211, 'postId': 43, 'email': 'Faustino.Keeling@morris.co.uk'},
    {'id': 212, 'postId': 43, 'email': 'Viola@aric.co.uk'},
    {'id': 213, 'postId': 43, 'email': 'Felton_Huel@terrell.biz'},
    {'id': 214, 'postId': 43, 'email': 'Ferne_Bogan@angus.info'},
    {'id': 215, 'postId': 43, 'email': 'Amy@reymundo.org'},
    {'id': 246, 'postId': 50, 'email': 'Jaycee.Turner@euna.name'},
    {'id': 281, 'postId': 57, 'email': 'Bridie@pearl.ca'},
    {'id': 282, 'postId': 57, 'email': 'Aglae_Goldner@madisyn.co.uk'},
    {'id': 316, 'postId': 64, 'email': 'Sister.Morissette@adelia.io'},
    {'id': 317, 'postId': 64, 'email': 'Shyanne@rick.info'},
    {'id': 318, 'postId': 64, 'email': 'Freeman.Dare@ada.name'},
    {'id': 351, 'postId': 71, 'email': 'Solon.Goldner@judah.org'},
    {'id': 352, 'postId': 71, 'email': 'Nina@osbaldo.name'},
    {'id': 353, 'postId': 71, 'email': 'Madaline@marlin.org'},
    {'id': 354, 'postId': 71, 'email': 'Mike.Kozey@gladyce.us'},
    {'id': 386, 'postId': 78, 'email': 'Alexandre@derrick.co.uk'},
    {'id': 387, 'postId': 78, 'email': 'Judd@lucinda.ca'},
    {'id': 388, 'postId': 78, 'email': 'Eleanora@karson.net'},
    {'id': 389, 'postId': 78, 'email': 'Enrico_Feil@liana.biz'},
    {'id': 390, 'postId': 78, 'email': 'Beverly@perry.org'},
    {'id': 421, 'postId': 85, 'email': 'Holden@kenny.io'},
    {'id': 456, 'postId': 92, 'email': 'Cassie@diana.org'},
    {'id': 457, 'postId': 92, 'email': 'Jena.OKeefe@adonis.net'},
    {'id': 491, 'postId': 99, 'email': 'Maxwell@adeline.me'},
    {'id': 492, 'postId': 99, 'email': 'Amina@emmet.org'},
    {'id': 493, 'postId': 99, 'email': 'Gilda@jacques.org'},
]


# ============================================================================
# 풀이
# ============================================================================
def index_users(users):
    # {id: name} 형태의 조회용 dict. 이게 있으면 매번 리스트를 뒤지지 않아도 된다.
    return {user['id']: user['name'] for user in users}


def count_comments(comments):
    result = {}

    for comment in comments:
        pid = comment['postId']
        # get(키, 기본값) 을 쓰면 키가 없을 때를 따로 처리하지 않아도 된다.
        result[pid] = result.get(pid, 0) + 1

    return result


def user_activity(users, posts, comments):
    names = index_users(users)
    per_post = count_comments(comments)

    # 모든 사용자를 0으로 초기화해 둔다. (글을 안 쓴 사람도 결과에 나와야 한다)
    stats = {}
    for user_id, name in names.items():
        stats[user_id] = {'name': name, 'posts': 0, 'comments': 0}

    for post in posts:
        uid = post['userId']
        stats[uid]['posts'] += 1
        # 이 글에 달린 댓글 수를 작성자에게 더한다. 댓글이 없는 글은 0.
        stats[uid]['comments'] += per_post.get(post['id'], 0)

    # 받은 댓글 내림차순, 같으면 이름 오름차순
    # -> 숫자는 부호를 뒤집고, 문자열은 그대로 두면 한 번에 정렬할 수 있다.
    return sorted(stats.values(), key=lambda s: (-s['comments'], s['name']))


def busiest_post(posts, comments, users):
    names = index_users(users)
    per_post = count_comments(comments)

    # 댓글 수 내림차순, 같으면 id 오름차순 -> 정렬 후 맨 앞
    ranked = sorted(posts, key=lambda p: (-per_post.get(p['id'], 0), p['id']))
    best = ranked[0]

    return {
        'title': best['title'],
        'author': names[best['userId']],
        'comments': per_post.get(best['id'], 0),
    }


if __name__ == '__main__':
    print('--- 1) 사용자 조회 dict ---')
    print(index_users(USERS))

    print('--- 2) 게시글별 댓글 수 ---')
    print(count_comments(COMMENTS))

    print('--- 3) 사용자별 활동 ---')
    for stat in user_activity(USERS, POSTS, COMMENTS):
        print(f"{stat['name']:<20} 글 {stat['posts']}개 / 받은 댓글 {stat['comments']}개")

    print('--- 4) 댓글이 가장 많은 글 ---')
    top = busiest_post(POSTS, COMMENTS, USERS)
    print(f"[{top['comments']}개] {top['title']} - {top['author']}")
