# 인접한 모든 자리수의 차이가 1인 수 계단수

# 길이가 N인 계단수 몇개
N = int(input())

dp = [[0] * 10 for _ in range(N+1)]

# 정답을 1000000000 으로 나눈 나머지
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    # 앞에 오는 숫자
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
