class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        all_nodes_cnt = 1
        node = self.head
        result_node = self.head
        while node.next is not None:
            node = node.next
            all_nodes_cnt += 1
        k_length = all_nodes_cnt - k
        print(f'all_nodes_cnt : {all_nodes_cnt} / k_length : {k_length}')  # 4
        for i in range(k_length):
            result_node = result_node.next
        return result_node

    def get_kth_node_from_last_2(self, k):
        min_k_point = self.head
        max_k_point = self.head
        for i in range(k):
            max_k_point = max_k_point.next  # k=2, max_k_point.data = 8
        while max_k_point is not None:
            min_k_point = min_k_point.next
            max_k_point = max_k_point.next
        return min_k_point

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(2).data)  # 9이(가) 나와야 합니다! 뒤에서 2번째.
print('---- 더 나은 방법 ----')
print(linked_list.get_kth_node_from_last_2(2).data)  # 9이(가) 나와야 합니다! 뒤에서 2번째.