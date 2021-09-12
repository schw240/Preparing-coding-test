N = int(input())

# N개의 수 입력
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

for n in nums:
    print(n, end=" ")
