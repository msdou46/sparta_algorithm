print('--------------------------- 4-6 DFS 구현해보기 - 재귀함수 ---------------------------')

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
visited = []
                        # 재귀함수는 후입선출. return 값이 있을 경우 재귀의 끝부터, 즉 나무의 끝 가지 부터 실행을 완료해 나가.
                        # 허나 재귀함수가 나뭇가지 처럼 펼쳐 나가는 과정에서 매개변수, 지역변수, 반환주소값 등은 모두 스택에 쌓이면서 진행.
def dfs_recursion(adjacent_graph, cur_node, visited_array):

    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:  # 예를 들어 cur_node 가 1이면, adjacent_node는 2, 5, 9 가 순차적으로 반영.
        if adjacent_node not in visited_array:  # adjacent_graph[cur_node]와 인접한 노드 중, 방문한 적이 없다면. 방문한 적이 있다면? 탈출.
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!