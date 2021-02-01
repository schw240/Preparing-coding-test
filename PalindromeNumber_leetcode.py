class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        if str_x[0].isdigit() == False:
            return False
        lst_x = list(str_x)
        dq = collections.deque(lst_x)

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
