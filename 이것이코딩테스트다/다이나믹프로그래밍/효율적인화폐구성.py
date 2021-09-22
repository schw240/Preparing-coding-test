N, M = map(int, input().split(' '))

# N가지 종류의 화폐를 이용해 개수를 최소한으로 해서 가치의 합이 M이 되도록 한다.

nums = []

for i in range(N):
    nums.append(int(input()))


# min값을 구해야하므로 0을 넣으면 안됌
INF = 999999
dp = [INF] * (M + 1)


dp[0] = 0
for i in range(N):
    for j in range(nums[i], M + 1):
        dp[j] = min(dp[j], dp[j - nums[i]] + 1)

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])
