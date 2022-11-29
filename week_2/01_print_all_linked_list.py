
print('----- Node -----')
class Node:
    def __init__(self, data):
        self.data = data        # 생성자 함수로 노드에 저장하고자 하는 데이터를 입력받고는 내부 변수에 저장.
        self.next = None        # 당장 처음 만드는 것이기에, 포인터로 가리킬 다음 노드는 지금으로서는 없어.

node = Node(3)
first_node = Node(4)
node.next = first_node   # node의 포인터에 first_node 라는 노드의 래퍼런스를 저장해 둔 거야.
print(node.next.data)
print(node.data) # 3


print('----- LinkedList -----')
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)      # 노드를 생성해서 연결하는데 위의 방식으로 Node를 생성하고 연결하고 하면 너무 귀찮잖아?
                                    # 그래서 링크드 리스트 클래스를 만들어서 관리를 해줄건데,
                                    # 링크드 리스트에서는 data 를 입력받고 이를 head 에 해당 data 를 들고 있는 Node 를 저장.
                                    # 이렇게 하면 링크드 리스트에 헤드 노드가 저장되는 거야.
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print(f'cur is {cur.data}')
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()





