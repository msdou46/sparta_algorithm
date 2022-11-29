print('--------------------------- 4-4 힙. 힙에 원소를 추가. ---------------------------')


class MaxHeap:
    def __init__(self):
        self.items = [None]  # 초기값으로 None 이 있는 이유는, 배열로 트리를 구성할 때에는 편의성을 위해 0번째 인덱스에 None 을 넣기 때문.

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1  # 방금 새로 append 한 요소의 인덱스.
        while cur_index > 1:
            parent_index = cur_index // 2  # 해당 노드의 부모 노드의 인덱스를 알아내는 법.
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index    # if문이 발동됬다는 건, 새로 입력한 값이 부모 노드의 요소 보다 크니 자리를 바꿨다는 뜻.
                                            # 따라서 새로 들어온 노드가 부모 노드가 되었다는 뜻.
                                            # while 을 계속 돌려 주면서 새로 들어온 노드가 부모 노드보다 값이 작을 때 까지 계속 자리를 바꿔줘.
                                            # 만약 그렇게 해서 최상위의 루트 노드까지 도달했다? 그럼 while 종료.
            else:
                break       # 새로 들어온 노드가 만약 자신보다 큰 부모를 만났다면? 그대로 break 하고 while 문 탈출.


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
