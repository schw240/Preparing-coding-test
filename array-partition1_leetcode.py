from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        # tmp = []
        
        # for n in nums:
        #     tmp.append(n)
        #     if len(tmp)==2:
        #         ans += min(tmp)
        #         tmp = []
        for i, n in enumerate(nums):
            if i % 2 == 0:
                ans += n
        return ans
        
s = Solution()
ans = s.arrayPairSum([1,4,3,2])
print(ans)