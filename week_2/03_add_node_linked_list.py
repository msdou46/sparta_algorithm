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
        for i in range(index - 1):  # index = 5   //  range(0, 4) => 0, 1, 2, 3 총 4번 구동. 1번째 head 에서 마지막인 5번째 까지 갈려면 4번 이동해야.
            if cur.next is None:
                print(f'node 의 총 갯수는 {max_index}개 입니다')
                break
            cur = cur.next
            max_index += 1
        return cur

    def add_node(self, index, value):
        new_node = Node(value)          # 우선 링크드 리스트에 추가하고 싶은 원소를 Node() 로 만들어.
        if index == 0:                  # 예외 처리. 만약 index가 0이라면? head node 로 놓고 싶은 것이라면?
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)   # 다음으로, 내가 (중간에) 삽입하고 싶은 index 번째의 노드를 저장해.
        next_node = node.next           # 마지막 준비로, node 의 바로 다음 노드를 미리 저장해 놔. 나중에 새로 삽입한 노드의 next에 래퍼런스를 저장해야 해.
        node.next = new_node
        new_node.next = next_node

linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(12)

linked_list.print_all()  # 5 6 7 8 12
linked_list.add_node(2, 11)
print('---- add_node 이후 -----')
linked_list.print_all()  # 5 6 11 7 9 12


