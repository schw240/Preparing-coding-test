# 계단은 한번에 하나 또는 둘
# 연속된 세개의 계단을 모두 밟아서는 안됨(시작점 제외)
# 마지막 계단은 반드시 밟기

# 계단수
n = int(input())
steps = [0 for _ in range(n+3)]
dp = [0 for _ in range(n+3)]
for i in range(1, n+1):
    steps[i] = int(input())

# 첫번째 계단
dp[1] = steps[1]
# 첫번째 -> 3번째
dp[2] = steps[1] + steps[2]
# 1 + 3 / 2 + 3 중 최대 경우
dp[3] = max(steps[1] + steps[3], steps[2] + steps[3])


for i in range(4, n+1):

    # 현재 계단을 선택했을때 이전 계단 선택?
    # 연속 3개는 안되므로 그 이전 dp값에 추가

    # 이전계단 안했을대는 2개 이전값에 추가
    dp[i] = max(dp[i-3] + steps[i-1] + steps[i], steps[i] + dp[i-2])

print(dp[n])
