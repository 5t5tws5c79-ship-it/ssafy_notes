"""
01. 유저 데이터 정제

> API 응답을 그대로 받은 USERS 는 한 사람의 정보가 dict 안에 dict 로 여러 겹 중첩되어 있다.
>
>     user['address']['geo']['lat']   ->  address 안의 geo 안의 lat
>                                          ⚠️ 이 값은 숫자가 아니라 '문자열' 이다!
>
> 아래 세 함수를 완성하시오.

---

1) flatten_users(users)
   깊이 파묻힌 값들을 꺼내 한 겹짜리 dict 리스트로 펼친다.
   lat, lng 는 문자열이므로 float 으로 변환해서 담을 것.

       [{'name': ..., 'email': ..., 'company': ..., 'city': ..., 'lat': ..., 'lng': ...}, ...]

2) filter_by_geo(flat_users, limit=80.0)
   위도와 경도의 절댓값이 모두 limit 미만인 사람만 남긴다.

3) group_by_hemisphere(flat_users)
   위도 부호로 남(S)/북(N), 경도 부호로 서(W)/동(E)를 정해
   'NE', 'NW', 'SE', 'SW' 네 그룹으로 이름을 모은다. (0 이상이면 N / E)
   각 그룹의 이름은 오름차순 정렬할 것.

       {'NE': ['Kurtis Weissnat'], 'SW': ['Clementine Bauch', ...], ...}
"""

# ============================================================================
# 연습용 데이터 (https://jsonplaceholder.typicode.com/users 의 실제 응답)
# 읽고 넘어가면 된다. 문제는 아래 함수부터.
# ============================================================================
USERS = [
    {
        'id': 1,
        'name': 'Leanne Graham',
        'email': 'Sincere@april.biz',
        'address': {
            'street': 'Kulas Light',
            'city': 'Gwenborough',
            'geo': {'lat': '-37.3159', 'lng': '81.1496'},
        },
        'company': {
            'name': 'Romaguera-Crona',
            'catchPhrase': 'Multi-layered client-server neural-net',
        },
    },
    {
        'id': 2,
        'name': 'Ervin Howell',
        'email': 'Shanna@melissa.tv',
        'address': {
            'street': 'Victor Plains',
            'city': 'Wisokyburgh',
            'geo': {'lat': '-43.9509', 'lng': '-34.4618'},
        },
        'company': {
            'name': 'Deckow-Crist',
            'catchPhrase': 'Proactive didactic contingency',
        },
    },
    {
        'id': 3,
        'name': 'Clementine Bauch',
        'email': 'Nathan@yesenia.net',
        'address': {
            'street': 'Douglas Extension',
            'city': 'McKenziehaven',
            'geo': {'lat': '-68.6102', 'lng': '-47.0653'},
        },
        'company': {
            'name': 'Romaguera-Jacobson',
            'catchPhrase': 'Face to face bifurcated interface',
        },
    },
    {
        'id': 4,
        'name': 'Patricia Lebsack',
        'email': 'Julianne.OConner@kory.org',
        'address': {
            'street': 'Hoeger Mall',
            'city': 'South Elvis',
            'geo': {'lat': '29.4572', 'lng': '-164.2990'},
        },
        'company': {
            'name': 'Robel-Corkery',
            'catchPhrase': 'Multi-tiered zero tolerance productivity',
        },
    },
    {
        'id': 5,
        'name': 'Chelsey Dietrich',
        'email': 'Lucio_Hettinger@annie.ca',
        'address': {
            'street': 'Skiles Walks',
            'city': 'Roscoeview',
            'geo': {'lat': '-31.8129', 'lng': '62.5342'},
        },
        'company': {
            'name': 'Keebler LLC',
            'catchPhrase': 'User-centric fault-tolerant solution',
        },
    },
    {
        'id': 6,
        'name': 'Mrs. Dennis Schulist',
        'email': 'Karley_Dach@jasper.info',
        'address': {
            'street': 'Norberto Crossing',
            'city': 'South Christy',
            'geo': {'lat': '-71.4197', 'lng': '71.7478'},
        },
        'company': {
            'name': 'Considine-Lockman',
            'catchPhrase': 'Synchronised bottom-line interface',
        },
    },
    {
        'id': 7,
        'name': 'Kurtis Weissnat',
        'email': 'Telly.Hoeger@billy.biz',
        'address': {
            'street': 'Rex Trail',
            'city': 'Howemouth',
            'geo': {'lat': '24.8918', 'lng': '21.8984'},
        },
        'company': {
            'name': 'Johns Group',
            'catchPhrase': 'Configurable multimedia task-force',
        },
    },
    {
        'id': 8,
        'name': 'Nicholas Runolfsdottir V',
        'email': 'Sherwood@rosamond.me',
        'address': {
            'street': 'Ellsworth Summit',
            'city': 'Aliyaview',
            'geo': {'lat': '-14.3990', 'lng': '-120.7677'},
        },
        'company': {
            'name': 'Abernathy Group',
            'catchPhrase': 'Implemented secondary concept',
        },
    },
    {
        'id': 9,
        'name': 'Glenna Reichert',
        'email': 'Chaim_McDermott@dana.io',
        'address': {
            'street': 'Dayna Park',
            'city': 'Bartholomebury',
            'geo': {'lat': '24.6463', 'lng': '-168.8889'},
        },
        'company': {
            'name': 'Yost and Sons',
            'catchPhrase': 'Switchable contextually-based project',
        },
    },
    {
        'id': 10,
        'name': 'Clementina DuBuque',
        'email': 'Rey.Padberg@karina.biz',
        'address': {
            'street': 'Kattie Turnpike',
            'city': 'Lebsackbury',
            'geo': {'lat': '-38.2386', 'lng': '57.2232'},
        },
        'company': {
            'name': 'Hoeger LLC',
            'catchPhrase': 'Centralized empowering task-force',
        },
    },
]


# ============================================================================
# 여기부터 문제
# ============================================================================
def flatten_users(users):
    result = []

    for user in users:
        # 중첩된 dict 는 대괄호를 이어 붙여 안쪽으로 파고든다.
        #   user['address']['geo']['lat']  ->  address 안의 geo 안의 lat
        pass

    return result


def filter_by_geo(flat_users, limit=80.0):
    # 절댓값은 abs() 를 사용한다.
    pass


def group_by_hemisphere(flat_users):
    result = {}

    for user in flat_users:
        # 1) 이 사람이 속한 그룹 키('NE' 등)를 만든다.
        # 2) result 에 그 키가 아직 없다면 빈 리스트를 먼저 넣어준다.
        # 3) 이름을 추가한다.
        pass

    # 각 그룹 안에서 이름 정렬

    return result


if __name__ == '__main__':
    flat = flatten_users(USERS)

    print('--- 1) 평탄화 (앞 2명) ---')
    for user in flat[:2]:
        print(user)
    # {'name': 'Leanne Graham', 'email': 'Sincere@april.biz',
    #  'company': 'Romaguera-Crona', 'city': 'Gwenborough',
    #  'lat': -37.3159, 'lng': 81.1496}
    # {'name': 'Ervin Howell', ... 'lat': -43.9509, 'lng': -34.4618}

    print('--- 2) 위/경도 필터 ---')
    near = filter_by_geo(flat)
    print(f'{len(flat)}명 중 {len(near)}명')       # 10명 중 6명
    for user in near:
        print(f"{user['name']:<20} ({user['lat']}, {user['lng']})")

    print('--- 3) 반구별 그룹 ---')
    groups = group_by_hemisphere(flat)
    for key in sorted(groups):
        print(key, groups[key])
    # NE ['Kurtis Weissnat']
    # NW ['Glenna Reichert', 'Patricia Lebsack']
    # SE ['Chelsey Dietrich', 'Clementina DuBuque', 'Leanne Graham', 'Mrs. Dennis Schulist']
    # SW ['Clementine Bauch', 'Ervin Howell', 'Nicholas Runolfsdottir V']
