from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(s)
        s.reverse()
        return s
s = Solution().reverseString(["h","e","l","l","o"])
print(s)