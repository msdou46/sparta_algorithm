from collections import deque

print('------------------- 5-6 삼성 역량 테스트 2 - 구슬 탈출 -------------------')

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
# 북, 동, 남, 서       시계 방향.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    # 벽이 아닐 때 까지, 현재 있는 곳이 탈출구가 아닐 때 까지 이동할거야.
    move_count = 0
    # 이 변수는 왜 필요 한가? 예를 들어서, 빨간 구슬과 파란 구슬이 동일 선상에 있어서, 위치가 곂칠 수가 있잖아? 근데 두 구슬은 한 칸에 함께 있을 수 없어.
    # 그래서, 나중에 해당 칸에 도착한, 바꿔 말하면 "더 많이 움직여서 해당 칸에 도착한" 구슬을 자신이 전진해 온 방향으로 한 칸 뒤로 물러나게 해줄거야.
    # 즉, 먼저 도촉한 구슬이 있으면, 나중에 도착한 구슬은 먼저 도착했던 구슬 때문에 그 전 칸에서 멈추게 된다는 거지.
    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "O":
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])  # 우선 game_map 의 행과 열의 크기를 구한다. 행과 열.
    queue = deque()  # 빨간 구슬의 경우의 수를 BFS 로 탐색을 하는 과정에서 어느 경우를 시험해 볼 것인지에 대해 큐를 쌓을 거야.
    visited = [
        [
            [
                [False] * m for _ in range(n)
            ] for _ in range(m)
        ] for _ in range(n)
    ]
    # 문제의 특성 상 규칙을 찾아보긴 어려워. 그래서 모든 경우의 수를 계산해서, 그 중에서 10번의 움직임 안에 빨간 구슬이 게임판을 탈출하는 수를 계산해야 해.
    # 모든 경우의 수를 구한다, 즉 BFS. 그리고 BFS는 큐를 사용해. 그리고 큐와 연동하기 위한 visitied 라는, 구슬이 지나간 위치를 저장해 주는 변수가 필요해.
    # 이번 문제에서 visited 는 4차원 배열로 구성할 거야. 왜? 공이 두 개니까.

    # 이제, BFS에서 탐색을 원활하게 하기 위해선 큐에다가 지금 어딜 시도해 볼 것인지에 대해 데이터를 쌓아 줘야 해. 빨간 구슬, 파란 구슬의 위치를 동시에 넣을 거야.
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1  # 먼저, 빨간 구슬과 파란 구슬의 좌표를 찾아 줄건데, 우선 초기화.
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j  # game_map 에서 빨간 구슬의 위치를 찾아 내.
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j  # game_map 에서 파란 구슬의 위치를 찾아 내.

    # 탐색을 10번 까지만 할 수 있어. 따라서 큐에 탐색하는 숫자도 넣어 줘야 해. 각 구슬의 위치를 한 번 탐색했다 치고 1.
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    # 큐에도 최초 빨간 구슬, 파란 구슬 위치를 넣었고, visited 에도 해당 위치를 검사했다고 추가했어. 이제 본격적으로 탐색.
    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count == 10:  # 만약 기울기 시도를 10번 했는 데도 빨간 구슬을 탈출시키지 못했다? 그냥 return False
            break

        # 네 방향으로 기울기 시도를 해야 해. 모든 경우의 수에 의거하여.
        for i in range(4):  # 네 방향으로 기울릴 수 있어. i가 0,1,2,3 인데, 북쪽부터 시작해서 시계방향으로.
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            # 현재 위치는 어디인지, 어느 방향을 볼 예정인지 입력. 그리고 이동한 끝에 무엇이 있는지 알기 위해 map 도 입력.
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)
            # 파란 구슬도 기울기와 함께 움직여야 해.

            if game_map[next_blue_row][next_blue_col] == 'O':  # 만약 파란 구슬이 먼저 구멍으로 빠졌다? 망했어.
                continue
            if game_map[next_red_row][next_red_col] == 'O':  # 만약 빨간 구슬이 구멍에 도착했다? 게임 끝!
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                # 만약 두 구슬의 위치가 동일하다? 보다 더 나중에 도착한 구슬의 위치를 한 칸 이전 으로 옮겨줘.
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                # 새롭게 기울린 뒤 각 구슬들이 도착한 좌표가 처음 방문한 곳 이라면? visited에 넣어주고, 큐에도 쌓아 줘야 해.
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))

game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))
