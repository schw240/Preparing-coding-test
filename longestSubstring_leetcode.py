class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        result = 1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    break
                else:
                    result = max(result, len(s[i:j+1]))
        return result
