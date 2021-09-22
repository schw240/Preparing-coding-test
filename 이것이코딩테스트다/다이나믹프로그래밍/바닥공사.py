N = int(input())

# 가로 길이가 N, 세로 길이가 2인 직사각형의 얇은 바닥이 있다.
# 2 X N 크기의 바닥을 채우는 방법의 수를 796796으로 나눈 나머지 출력

dp = [0] * 1001

# 1은 2X1만 가능
# 2는 1X2, 2X1 2개, 2X2 1개 가능

dp[1] = 1
dp[2] = 3
dp[3] = 5
# i-1 + i-2 * 2
for i in range(4, N+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[N])
