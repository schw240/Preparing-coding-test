class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1 is not None:
            num1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2.append(l2.val)
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        #print(num1, num2)
        res1=int(''.join(map(str,num1)))
        res2=int(''.join(map(str,num2)))
        #print(res1, res2)
        res3=str(res1+res2)
        l3=None
        for i in res3:
            data=int(i)
            newnode=ListNode(data)
            if not l3:
                l3=newnode
            else:
                newnode.next=l3
                l3=newnode
        return l3

print(Solution().addTwoNumbers([2,4,3], [5,6,4]))