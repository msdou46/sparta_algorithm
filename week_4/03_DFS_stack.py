print('--------------------------- 4-6 DFS 구현해보기 - 스택 ---------------------------')

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

def dfs_stack(adjacent_graph, start_node):

    stack = [start_node]    # 1  앞으로 인접한 노드들을 처음 발견하면 스택에 넣을꺼야.
    visited_array = []      # 재귀때와 마찬가지로, 방문한 노드들을 넣을거야.

    while stack:
        current_node = stack.pop()  # 처음에는 1. stack 에는 기본적으로 방문한 적이 없는 노드들이 쌓여 있어.
        visited_array.append(current_node)      # 인접한 노드들(방문하지 않은)을 stack 에 넣어 뒀다가, 방문함과 당시에 visited 에 넣어줘.
        for adjacent_node in adjacent_graph[current_node]:  # 이번에 방문한 노드의 인접한 노드들을 하나 하나 검색
            if adjacent_node not in visited_array:          # 방문한 적이 없다?
                stack.append(adjacent_node)             # 스택에 쌓아 둔다.

    return visited_array

print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!