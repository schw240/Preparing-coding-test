# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        data = []

        # 노드 안에 있는 데이터들 넣어주기
        for node in lists:
            while node:
                heapq.heappush(data, node.val)
                node = node.next
        print(data, "data")

        while data:
            val = heapq.heappop(data)
            current.next = ListNode(val)
            current = current.next
        return dummy.next
