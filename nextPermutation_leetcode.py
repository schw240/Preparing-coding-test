class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                start = i-1
                # print("start", i-1)

                for k in range(len(nums)-1, start, -1):
                    if nums[k] > nums[start]:
                        # print("end", k)
                        end = k

                        nums[start], nums[end] = nums[end], nums[start]

                        for m in range(int((len(nums)-start)/2)):
                            # print(start+1+m, len(nums)-1-m)
                            nums[start+1+m], nums[len(nums)-1 -
                                                  m] = nums[len(nums)-1-m], nums[start+1+m]

                        # print(nums)
                        break
                break
            if i == 1:
                nums.reverse()
