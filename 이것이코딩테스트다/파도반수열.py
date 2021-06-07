# 나선에서 가장 긴 변의 길이를 k
# 그 변에 길이가 k인 정삼각형 추가

dp = [0] * 101
dp[1] = 1
dp[2] = 1


def P(N):
    for i in range(3, N+1):
        dp[i] = dp[i-3] + dp[i-2]
    return dp


T = int(input())

for i in range(T):
    N = int(input())
    dp = P(N)
    print(dp[N])
