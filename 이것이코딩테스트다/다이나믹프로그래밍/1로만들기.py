X = int(input())

dp = [0] * 30001

# 5로 나누어 떨어지면 5로, 3으로 나누어 떨어지면 3으로, 2로 나누어 떨어지면 2로, 안된다면 1 빼기

for i in range(2, X + 1):
    dp[i] = dp[i-1] + 1

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[X])
