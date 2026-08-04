"""
02. 게시글 / 댓글 집계

> 서로 다른 세 개의 리스트가 있다. 이들은 id 로 연결되어 있다.
>
>     USERS    : {'id': 1, 'name': 'Leanne Graham'}
>     POSTS    : {'id': 1, 'userId': 1, 'title': '...'}   # userId -> USERS 의 id
>     COMMENTS : {'id': 1, 'postId': 1, 'email': '...'}   # postId -> POSTS 의 id
>
> "어느 사용자가 쓴 글에 댓글이 가장 많이 달렸는가?" 를 알아내려면
> 세 리스트를 id 로 이어 붙여야(join) 한다. 아래 네 함수를 완성하시오.

---

1) index_users(users)
   {사용자id: 이름} 형태의 dict 를 만든다. 매번 리스트를 처음부터 뒤지지 않기 위한 조회표.

       {1: 'Leanne Graham', 2: 'Ervin Howell', ...}

2) count_comments(comments)
   {게시글id: 그 글에 달린 댓글 수} 형태의 dict 를 만든다.

       {1: 4, 8: 5, 15: 1, ...}

3) user_activity(users, posts, comments)
   사용자별로 쓴 글 수와 받은 댓글 수를 집계한다.
   글을 하나도 안 쓴 사람도 0 으로 결과에 포함할 것.
   정렬은 [받은 댓글 수 내림차순], 같으면 [이름 오름차순].

       [{'name': ..., 'posts': 2, 'comments': 9}, ...]

4) busiest_post(posts, comments, users)
   댓글이 가장 많이 달린 글 하나를 찾아 아래 형태로 반환한다.
   댓글 수가 같다면 id 가 작은 글을 고를 것.

       {'title': ..., 'author': ..., 'comments': 5}
"""

# ============================================================================
# 연습용 데이터 (jsonplaceholder.typicode.com 의 실제 응답에서 추린 것)
# 읽고 넘어가면 된다. 문제는 아래 함수부터.
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
# 여기부터 문제
# ============================================================================
def index_users(users):
    # dict 컴프리헨션 {키: 값 for ...} 을 쓰면 한 줄로도 된다.
    pass


def count_comments(comments):
    result = {}

    for comment in comments:
        # 처음 보는 게시글이면 0 부터, 이미 있으면 1 더하기
        # 힌트) result.get(키, 0) 을 쓰면 두 경우를 한 줄로 처리할 수 있다.
        pass

    return result


def user_activity(users, posts, comments):
    # 1) {사용자id: {'name': ..., 'posts': 0, 'comments': 0}} 로 전원을 0 초기화
    # 2) POSTS 를 돌면서 작성자에게 글 수 +1, 그 글의 댓글 수만큼 댓글 수 +N
    # 3) 정렬해서 리스트로 반환
    #    힌트) sorted(..., key=lambda s: (-s['comments'], s['name']))
    #          숫자에 - 를 붙이면 그 항목만 내림차순이 된다.
    pass


def busiest_post(posts, comments, users):
    # 정렬 후 맨 앞을 고르거나, max() 에 key 를 넘겨도 된다.
    pass


if __name__ == '__main__':
    print('--- 1) 사용자 조회 dict ---')
    print(index_users(USERS))
    # {1: 'Leanne Graham', 2: 'Ervin Howell', ... , 10: 'Clementina DuBuque'}

    print('--- 2) 게시글별 댓글 수 ---')
    print(count_comments(COMMENTS))
    # {1: 4, 8: 5, 15: 1, 22: 2, 29: 3, 36: 4, 43: 5, 50: 1,
    #  57: 2, 64: 3, 71: 4, 78: 5, 85: 1, 92: 2, 99: 3}

    print('--- 3) 사용자별 활동 ---')
    for stat in user_activity(USERS, POSTS, COMMENTS):
        print(f"{stat['name']:<20} 글 {stat['posts']}개 / 받은 댓글 {stat['comments']}개")
    # Leanne Graham        글 2개 / 받은 댓글 9개
    # Nicholas Runolfsdottir V 글 2개 / 받은 댓글 9개   <- 9개 동점, 이름 순으로 뒤
    # Chelsey Dietrich     글 2개 / 받은 댓글 6개
    # ... (총 10명)
    # Glenna Reichert      글 1개 / 받은 댓글 1개

    print('--- 4) 댓글이 가장 많은 글 ---')
    top = busiest_post(POSTS, COMMENTS, USERS)
    print(f"[{top['comments']}개] {top['title']} - {top['author']}")
    # [5개] dolorem dolore est ipsam - Leanne Graham
