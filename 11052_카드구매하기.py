N = int(input())
pn = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = pn[1]

# dp[1] = 1 1번카드 1개
# dp[2] = 2 2번카드 1개 , 1번카드 2개
# dp[3] = 3 3번카그 1개, 2번카드 1개 1번카드 1개, 1번카드 3개
# dp[N] = N N번카드 1개, dp[N-1] + dp[1], dp[N-2] + dp[2] .. dp[N-i] + dp[i]


for i in range(2, N+1):
    dp[i] = pn[i]
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp[N])
