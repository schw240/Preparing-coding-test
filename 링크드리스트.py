# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Node:
    # 만약 인자가 2개가 들어오면 next를 넣어주고
    # 인자가 하나만 들어온다면 next는 None이 됨
    # default값이 None이라는 의미
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data):
    # 맨 앞의 노드에 head 연결
    node = head
    while node.next:
        node = node.next
    # 여기까지 오면 마지막 노드
    # 마지막 노드의 next에 data 연결
    node.next = Node(data)


node1 = Node(1)
head = node1
for index in range(1, 10):
    add(index)

# node = head
# while node.next:
#     print(node.data)
#     node = node.next
# print(node.data)

node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
