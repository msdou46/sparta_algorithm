print('--------------------------- 3-5 스택 ---------------------------')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # push. 맨 앞(위)에 데이터 넣기.
    def push(self, value):  # 만약 처음에 [4] 만 있었다면, [3] -> [4] 이렇게 만들어주는 거지. head 자리를 새치기 하는거야. 왜? 후입선출.
        new_head = Node(value)
        new_head.next = self.head   # 먼저 기존의 head 를 새로운 node 의 next 에 연결 해주고
        self.head = new_head        # 새로 입력한 node 를 head 로 선정.

    # pop. 맨 앞의 데이터를 지우 면서 리턴으로 가져옴.
    def pop(self):
        if self.is_empty(): # 스택이 비어있다면?
            return "현재 스택에는 아무것도 저장되어 있지 않습니다."
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    # peek. 맨 앞의 데이터 보기.
    def peek(self):
        if self.is_empty():
            return "현재 스택에는 아무것도 저장되어 있지 않습니다."
        return self.head.data

    # isEmpty. 스택이 비었는지 안 비었는지 여부를 판별.
    def is_empty(self):
        return self.head is None   # None 이라면 비어 있으니까 true 를 반환 하겠지. 있으면 false 를 반환하고.


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.push(5)
print(stack.pop().data)
print('가장 위에 있는 스택은? ', stack.peek())
print('현재 스택은 비어있는가? ', stack.is_empty())



'''
강창민 튜터님 알고리즘 수업 실습

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, data):
        self.head = Node(data)

    def peek(self):
        return self.head

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return (우선 스택 된 노드가 있는 지 부터 체크합니다.)
        pop_node = self.head
        self.head = self.head.next
        return pop_node


pop
1. 스택은 선입후출 이기 때문에, 넣을 때도 head로, 지울 때도 head 부터 삭제합니다.
2. 우선 스택 된 노드가 있는 지 부터 체크합니다. 있을 경우, 메소드를 계속해서 실행합니다.
3. 우선 pop_node 라는 변수에 head 에 저장된 노드의 주소를 저장해 줍니다.
4. 그리고 기존의 head 노드의 next 에 저장되어 있던 (맨 위에서 두 번째) 노드가 새롭게 head 로 올라갑니다.
5. 마지막으로, 삭제할 pop_node 를 리턴해 줍니다. 이로서 스택 공간에서 가장 위에 있던 노드가 적출됩니다.



push
1. 만약 stack = Stack(3) 이런 식으로 클래스 인스턴스가 선언되어 있다면,
    stack.push(4) 이렇게 인스턴스에 접근하여 push 메소드를 호출할 수 있도록 하겠습니다.
2. push() 메소드는 인자로서 새롭게 입력할 데이터를 받고, 그 데이터를 self.data 로 갖는 노드를 생성합니다.
3. 우선 새롭게 생성한 Node(data) 를 변수에 저장합니다.
    그리고 새롭게 생성한 노드의 next에는, 기존의 self.head의 주소를 저장해 줍니다.
4. 그리고 최종적으로는 새로운 노드가 self.head 에 등록됩니다.

peek
1. Stack 클래스는 데이터를 인자로 입력받아 Node 를 생성합니다.
    최초의 생성이면, 해당 클래스 인스턴스의 head, 즉 첫 번째 노드로 지정합니다.
2. peek() 이라는 메소드는 가장 위에 있는 노드, 즉 head 노드를 반환합니다.
3. 하지만 만약 인스턴스가 만들어져 있지 않을 경우, 혹은 예상치 못한 변수로 인해
    head node 가 없다면, 이를 위한 예외 처리가 필요할 것 같습니다.
    

'''