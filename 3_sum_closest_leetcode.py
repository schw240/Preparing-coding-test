class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()

        for idx, num in enumerate(nums):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]

                if abs(target - three_sum) < abs(diff):
                    diff = target - three_sum

                if three_sum > target:
                    right -= 1
                else:
                    left += 1
            if diff == 0:
                break
        return target - diff
