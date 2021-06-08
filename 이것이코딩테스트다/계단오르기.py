n = int(input())

dp = [0 for _ in range(n + 2)]
steps = [0 for _ in range(n + 2)]

for i in range(1, n+1):
    steps[i] = int(input())

# 첫번째 계단은 무조건
dp[1] = steps[1]
# 1 + 2
dp[2] = steps[1] + steps[2]
# 1 + 3 or 2 = 3
dp[3] = max(steps[1] + steps[2], steps[2] + steps[3])

for i in range(4, n + 1):
    # 이전계단 선택한 경우 , 그 이전 계단 선택한 경우
    # 이전계단은 연속 3개가 안되므로 그 전전 계단 값과 더해주기
    dp[i] = max(dp[i-3] + steps[i] + steps[i-1],
                steps[i] + dp[i-2])

print(dp[n])
