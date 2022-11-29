from collections import deque

print('--------------------------- 5-2 2019년 상반기 LINE 인턴 채용 코딩테스트 - 나 잡아봐라  ---------------------------')

c = 11
b = 2


def catch_me(cony_loc, brown_loc):

    time = 0    # 코니와 브라운이 동일한 시간대에 각각 어느 위치에 있는지 알아야 해.
    queue = deque()
    queue.append((brown_loc, 0))    # 초기값으로 브라운의 위치와 시간인 0을 담아줘. 왜? 위치와 시간이 동시에 일치해야지만 서로가 만난 것이기에.
    visited = [{} for _ in range(200001)]   # 각 초에 어느 곳을 갔는지를 저장하기 위한 시간. 우선 20만개의 딕셔너리를 배열에 삽입.


    while cony_loc <= 200000:   # 코니의 이동거리가 20만을 넘어가면 너무 멀리 달아나는 것이기에 그냥 게임이 끝나버려.
        cony_loc += time    #   코니의 이동 거리는 매 초마다 1씩 늘어나니까, 시간만큼 더해 주면 돼.

        if time in visited[cony_loc]:       # 코니의 위치
            return time

        for i in range(0, len(queue)):  # 현재 queue의 길이만큼 반복을 할거야.
            current_position, current_time = queue.popleft()    # 큐에서 브라운의 위치와 시간을 가져와서 '현재' 위치, '현재' 시간으로 사용.

            new_time = current_time + 1                 # 브라운이 움직일 수 있는 경우의 수를 모두 큐에 저장.
            brown_new_position = current_position - 1

            if brown_new_position >= 0 and new_time not in visited[brown_new_position]:
                visited[brown_new_position][new_time] = True
                queue.append((brown_new_position, new_time))

            brown_new_position = current_position + 1
            if brown_new_position < 200001 and new_time not in visited[brown_new_position]:
                visited[brown_new_position][new_time] = True
                queue.append((brown_new_position, new_time))

            brown_new_position = current_position * 2
            if brown_new_position < 200001 and new_time not in visited[brown_new_position]:
                visited[brown_new_position][new_time] = True
                queue.append((brown_new_position, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
