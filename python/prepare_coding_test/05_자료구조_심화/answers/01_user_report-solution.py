"""
01. 유저 데이터 정제 - 풀이
"""

# ============================================================================
# 연습용 데이터 (https://jsonplaceholder.typicode.com/users 의 실제 응답)
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
# 풀이
# ============================================================================
def flatten_users(users):
    result = []

    for user in users:
        # 중첩된 dict 는 대괄호를 이어 붙여 안쪽으로 파고든다.
        #   user['address']['geo']['lat']  ->  address 안의 geo 안의 lat
        result.append({
            'name': user['name'],
            'email': user['email'],
            'company': user['company']['name'],
            'city': user['address']['city'],
            # 원본 데이터에서 위/경도는 문자열이므로 float 으로 바꿔 담는다.
            'lat': float(user['address']['geo']['lat']),
            'lng': float(user['address']['geo']['lng']),
        })

    return result


def filter_by_geo(flat_users, limit=80.0):
    # 조건에 맞는 것만 남기는 전형적인 리스트 필터링
    return [u for u in flat_users if abs(u['lat']) < limit and abs(u['lng']) < limit]

    # 반복문으로 쓰면 아래와 같다.
    # result = []
    # for u in flat_users:
    #     if abs(u['lat']) < limit and abs(u['lng']) < limit:
    #         result.append(u)
    # return result


def group_by_hemisphere(flat_users):
    result = {}

    for user in flat_users:
        # 위도 부호로 남/북, 경도 부호로 동/서를 정한다.
        key = ('N' if user['lat'] >= 0 else 'S') + ('E' if user['lng'] >= 0 else 'W')

        # 키가 없으면 빈 리스트를 먼저 만들어 준다. (setdefault 로도 가능)
        if key not in result:
            result[key] = []
        result[key].append(user['name'])

    # 각 그룹 안에서 이름을 오름차순 정렬
    for key in result:
        result[key].sort()

    return result


if __name__ == '__main__':
    flat = flatten_users(USERS)

    print('--- 1) 평탄화 (앞 2명) ---')
    for user in flat[:2]:
        print(user)

    print('--- 2) 위/경도 필터 ---')
    near = filter_by_geo(flat)
    print(f'{len(flat)}명 중 {len(near)}명')
    for user in near:
        print(f"{user['name']:<20} ({user['lat']}, {user['lng']})")

    print('--- 3) 반구별 그룹 ---')
    groups = group_by_hemisphere(flat)
    for key in sorted(groups):
        print(key, groups[key])
