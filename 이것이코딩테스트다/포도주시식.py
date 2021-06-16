# 선택 후 마신 후 원래 위치
# 연속 3잔은 X
# 가장 많은 양의 포도주 마시는 경우

n = int(input())
wine = [0]
dp = [0] * (n + 1)

for i in range(1, n+1):
    wine.append(int(input()))

dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

# 1
# w1

# 2
# w1 + w2

# 3
# w1 + w2, dp[2]
# w1 + w3
# w2 + w3

# 4
# w2 + w3, dp[3] -> dp[i-1]
# w1 + w3 + w4 -> dp[i-3] + w[i-1] + w[i]
# w1 + w2 + w4 -> dp[i-2] + w[i]

# dp[4-1], dp[4-3] + w[4-1] + w[4], dp[4-2] + w[4]
for i in range(3, n+1):
    # 연속 3잔 안됨
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
