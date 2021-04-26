nums = list(map(int, input().split()))
# print(nums)

des = False
asc = False
mix = False
for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
        asc = True

    if nums[i-1] > nums[i]:
        des = True

if asc == True and des == False:
    print("ascending")
if asc == False and des == True:
    print("descending")
if asc == True and des == True:
    print("mixed")
