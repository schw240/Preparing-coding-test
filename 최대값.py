nums = []
for i in range(9):
    nums.append((i, int(input())))

max = 0
ans_idx = -1
for i in range(len(nums)):
    if max < nums[i][1]:
        max = nums[i][1]
        ans_idx = i

print(max)
print(ans_idx+1)
