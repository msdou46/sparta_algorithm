print('--------------------------- 4-7 BFS 구현해보기 - 큐 ---------------------------')

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

def bfs_queue(adj_graph, start_node):

    queue = [start_node]   # 1  앞으로 인접한 노드들을 처음 발견하면 큐에 넣을꺼야.
    visited_node = []       # 방문한 노드 순서대로 배열에 추가.

    while queue:
        current_node = queue.pop(0)
        visited_node.append(current_node)
        for adj_node in adj_graph[current_node]:
            if adj_node not in visited_node:
                queue.append(adj_node)

    return visited_node

print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!