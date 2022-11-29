print('------------------- 5-5 삼성 역량 테스트 1 - 새로운 게임2 -------------------')

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    current_stacked_horse_map = [  # 체스판의 한 칸에서 말들이 중첩되어 쌓일 경우를 저장해 주기 위해서.
        [
            [] for _ in range(n)
        ] for _ in range(n)
    ]
    turn_count = 1
    for i in range(horse_count):  # 처음 말들이 시작 하는 위치를 current_stacked_horse_map 에 저장할거야.
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    while turn_count <= 1000:  # 이제 말들을 방향에 맞게 한 턴씩 한 턴씩 움직여 볼거야.
        for horse_index in range(horse_count):  # 각 말들. 이 경우 4개의 말들.
            n = len(game_map)
            r, c, d = horse_location_and_directions[horse_index]  # 처음 말들이 시작하는 위치와 바라보고 있는 방향.
            new_r = r + dr[d]  # 말들이 바라보고 있는 방향으로 한 칸 앞의 좌표. 한 턴 마다 한 칸 씩 이동해야 하니까.
            new_c = c + dc[d]

            # 새롭게 이동할 칸이 범위 밖 이거나, 파란색 칸일 경우.
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)
                horse_location_and_directions[horse_index][2] = new_d  # 반대 방향의 d 를 새롭게 갱신.
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 이동할 칸이 파란색이거나 막혀 있어서 반대로 돌아서 한 칸 갈려고 했는데, 그곳도 파란색이거나 막혀있다? 그럼 제자리에 가만히.
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue  # for문을 그냥 빠져나온다. 아무런 변동 없이.

            # 새로운 칸으로 이동하기 전에, 몇 가지 규칙을 이행 해야 해. 위에 쌓여져 있는 말이 있으면 같이 움직여야 한다는 것. 그리고 이동하려는 칸의 색깔도 고려.
            moving_horse_index_array = []  # 이동할 애들만 저장. 말이 이동할 땐 자기 위에 있는 말들과 함께 이동하니까.
            for i in range(len(current_stacked_horse_map[r][c])): # [[[0], [1], [2], []], [[], [], [], []], [[], [], [3], []], [[], [], [], []]]
                # 곂쳐져 있는 횟수 만큼 for문이 돌아간다.
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]  # 움직일 말들
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]  # 남을 말들
                    break

            if game_map[new_r][new_c] == 1:  # 이동하려는 칸이 빨간 칸일 경우, 배열을 뒤집어야 해.
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:  # 새롭게 이동한 칸에 말(혹은 중첩된 말들)을 이동시켜줘.
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][
                    1] = new_r, new_c
                # 말들의 현재 위치를 따로 저장한 배열에도 위치를 갱신해줘.

            # 턴이 진행 되는 중, 말이 4개가 쌓이는 순간 게임이 끝나.
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count

        turn_count += 1  # 게임이 계속 진행될 경우, 카운트가 1000까지 도달 해도 게임이 끝나지 않는 다면 게임을 그냥 종료.

    return turn_count


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야 합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
