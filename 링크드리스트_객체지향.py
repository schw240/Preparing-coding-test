class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:

    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            # 여기까지 오면 마지막 노드
            node.next = Node(data)

    # 순회 함수
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == "":
            print("해당 값을 가진 노드가 없습니다.")
            return
        # head 값 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        # 마지막 노드 삭제, 중간 노드 삭제
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


# linkedlist1 = NodeMgmt(0)
# linkedlist1.desc()

# for data in range(1, 10):
#     linkedlist1.add(data)

# linkedlist1.desc()


# 링크드리스트의 복잡한 기능
# 특정 노드 삭제

# 1. head 삭제
# 2. 마지막 노드 삭제
# 3. 중간 노드 삭제
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
linkedlist1.delete(0)
# linkedlist.desc() -> 여기서 오류가 뜨는데 해당 객체가 삭제되었단 의미 (구현 잘됨)
