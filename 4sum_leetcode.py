class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        if len(nums) < 4:
            return []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 첫번째 숫자
            choice1 = nums[i]
            for k in range(i+1, len(nums)):
                if k > i+1 and nums[k] == nums[k-1]:
                    continue
                # 두번째 숫자
                choice2 = nums[k]

                start = k+1
                end = len(nums)-1

                while start < end:
                    choice3 = nums[start]
                    choice4 = nums[end]

                    if choice1 + choice2 + choice3 + choice4 == target:
                        ans.append([choice1, choice2, choice3, choice4])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif choice1 + choice2 + choice3 + choice4 < target:
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    else:  # choice1 + choice2 + choice3 + choice4 > target
                        end -= 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1

        return ans
