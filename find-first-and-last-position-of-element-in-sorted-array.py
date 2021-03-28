class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                starting = i
                break
        else:
            return [-1, -1]

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                ending = i
                break

        return [starting, ending]
