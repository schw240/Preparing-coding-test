# 5로 나누어떨어지면 5로, 3으로 나누어떨어지면 3으로, 2로 나누어 떨어지면 2로 나눈다
# 아무것도 해당되지 않는다면 1을 뺀다
# 연산을 사용하는 최솟값을 출력하기

X = int(input())

dp = [0] * 30001

for i in range(2, X + 1):

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    dp[i] = dp[i-1] + 1

print(dp[X])
