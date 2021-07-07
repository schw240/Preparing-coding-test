n = int(input())

# 연속된 수의 합 중 가장 큰 값
nums = list(map(int, input().split(' ')))
dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    # 이전값에서 현재값더한 값, 현재값 중 최대값
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))
