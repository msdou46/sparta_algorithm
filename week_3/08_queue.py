
print('--------------------------- 3-6 큐 구현해보기 ---------------------------')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 데이터 추가하기
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node   # 기존의 self.tail에 저장되어 있던 노드에게 next 로 new_node 를 설정해주고
        self.tail = new_node        # self.tail 에는 new_node의 래퍼런스를 저장.
        return

    # 맨 앞의 데이터 뽑기. 선입 선출.
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        dequeue_node = self.head
        self.head = self.head.next
        return dequeue_node.data

    # 맨 앞의 데이터 보기
    def peek(self):
        if self.is_empty():
            return "queue is empty"
        return self.head.data

    # 큐가 비었는지 안 비었는지 여부
    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())

print('--- 선입선출로 잘 빠져 나오나? ---')
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())


