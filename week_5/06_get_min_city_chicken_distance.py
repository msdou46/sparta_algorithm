import itertools, sys

print('------------------- 5-7 삼성 역량 테스트 3 - 치킨 배달 -------------------')


n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):      # n = city_map 의 행과 열의 길이. m = 폐업시키지 않을 최대 치킨집의 개수
    # 우선 각 집들의 '치킨 거리' 의 최소 거리를 구하기 위해서 치킨 집들의 위치와 집들의 위치를 가져와 보자.
    chicken_location_list = []
    home_location_list = []

    for i in range(n):      # 우선 city_map 을 for 문을 돌며 탐색. 집과 치킨집을 찾을 때마다 배열에 append. 이러면 각 집들의 총 갯수와 위치를 찾아내.
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    # 이제 치킨 집들의 위치를 가지고 조합을 만들어 볼 거야. 모든 경우의 수 중에서 최대한 이득이 되는 경우를 찾아야 한다? 이럴 때는 '조합' 을 이용해야 해.
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
                # 예를 들자면, 지금 chicken_location_list는 [[1, 2], [2, 3], [4, 4], [5, 1]] 뭐 이런 식일 텐데,
                # m개로 조합할 수 있는 경우의 수를 모두 반환해. 또한 list 로 감싸야지 우리에게 익숙한 배열의 형태로 자료를 확인할 수 있어.
                # 예를 들어 m = 3 이다? [ ([1, 2], [2, 2], [4, 4]) ] 이렇게 경우의 수 한 개를 ()=튜플 로 묶어줘.
                # m = 2 라면? [ ([0, 1], [3, 0]), ([0, 1], [4, 0]), ([0, 1], [4, 1]), ... ]  이렇게 조합을 () 로 묶어 주지.
                # 위의 코드의 경우, chicken_location_list 배열의 각 구성 요소들인 [i, j] 들을 m개로 묶을 시의 경우의 수를 모두 보여주는거야.
                # 어쨌든 중요한 건 도시에 있는 총 치킨집 중에서 m개만 남기고 싶은데, m개만 남을 수 있는 경우의 수를 모두 구한거지.

    # 이제 위에서 만든 조합들을 가지고, 최소 '도시 치킨거리' 를 구해보자.
    min_distance_of_m_combinations = sys.maxsize    # 최솟값을 정해줘.

    for chicken_location_m_combination in chicken_location_m_combinations:  # m개만 남을 경우의 조합들을 하나씩 가져와. ([0, 1], [3, 0]) 이런 식
        city_chicken_distance = 0    # '도시의 치킨 거리' 의 총 합을 여기다가 저장해 줄 거야.

        # 각 집들의 '치킨 거리' 를 모두 합한 것이 '도시의 치킨 거리' 잖아? 즉, 일단 각 집들의 '치킨 거리' 를 모두 알아야 해.
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize     # 최솟값을 넣어줄 거야.
            for chicken_location in chicken_location_m_combination:  # m개의 치킨집의 조합 하나에서 각 치킨집들의 [r, c] 를 가져 와.
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])       # abs 는 절대값.
                )
            city_chicken_distance += min_home_chicken_distance       # 각 집의 최단 치킨 거리를 구하면, 그걸 distance 에 중첩으로 +.

        min_distance_of_m_combinations = min(       # 매 m개의 조합들이 '각 집들의 최단 치킨 거리의 총 합 = 도시의 치킨 거리' 를 구할 때마다,
            min_distance_of_m_combinations,         # 이전 조합의 '도시의 치킨 거리' 와 어느 쪽이 더 적은 수인지 비교해.
            city_chicken_distance                   # 이렇게 하면, 가장 '도시의 치킨 거리' 가 적은 조합의 '도시의 치킨 거리' 가 들어가 있어.
        )
    return min_distance_of_m_combinations


# 출력
print('---- 1 ----')
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print('---- 2 ----')
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print('---- 3 ----')
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))

