from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

    #     for i in range(len(nums)-2):
    #         if(i > 0 and nums[i] == nums[i-1]):
    #             continue
    #         for j in range(i+1, len(nums)-1):
    #             if(j > i+1 and nums[j] == nums[j-1]):
    #                 continue
    #             for k in range(j+1, len(nums)):
    #                 if(k > j+1 and nums[k] == nums[k-1]):
    #                     continue
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     res.append((nums[i], nums[j], nums[k]))
    #     return res
#시간초과뜸
        for i in range(len(nums) - 2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            left, right = i+1, len(nums) -1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
        



s = Solution()
ans = s.threeSum([-1, 0, 1, 2, -1, -4])
print(ans)