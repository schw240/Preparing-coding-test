# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = None

        vallist = []
        #print(head, "head")
        while True:
            vallist.append(head.val)
            head = head.next
            if head == None:
                break

        outlist = vallist[0:len(vallist)-n] + vallist[len(vallist)-n+1:]
        print(outlist)
        for i in range(len(outlist)-1, -1, -1):
            temp = ListNode(outlist[i])
            print(temp, "temp")
            temp.next = ans
            print(ans, "ans")
            ans = temp
            print(ans, "ans down")
        return ans
