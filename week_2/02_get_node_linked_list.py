class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        max_index = 1
        for i in range(index-1): #index = 5   //  range(0, 4) => 0, 1, 2, 3 총 4번 구동. 1번째 head 에서 마지막인 5번째 까지 갈려면 4번 이동해야.
            if cur.next is None:
                print(f'node 의 총 갯수는 {max_index}개 입니다')
                break
            cur = cur.next
            max_index += 1
        return cur

linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(12)

print('결과값', linked_list.get_node(7).data) # -> 6를 들고 있는 노드를 반환해야 합니다!