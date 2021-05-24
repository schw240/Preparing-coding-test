# N+1일째 되는 날 퇴사를 하기 위해 남은 N일동안 최대한 많은 상담을 함
N = int(input())
# 상담을 완료하는데 걸리는 기간 T와 상담을 했을 때 받을 수 있는 금액 P
T = []
P = []
for i in range(N):
    a, b = map(int, input().split(' '))
    T.append(a)
    P.append(b)

# i 번째 날까지 일을 했을 때 최대값을 보관할 dp 배열
dp = [0 for _ in range(N+2)]

# for i in range(N - 1, -1, -1):
#     # 오늘 날짜가 가능한지 안한지 비교후 선택
#     if T[i] + i <= N:
#         # 돈 P[i] + 날짜 dp[i + T[i]], 그리고 다음날의 값과 비교
#         dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
#     # 날짜 선택하지 않을 경우
#     else:
#         dp[i] = dp[i+1]

for i in range(N):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]

    if i + T[i] <= N:
        if dp[i + T[i]] < P[i] + dp[i]:
            dp[i + T[i]] = P[i] + dp[i]

# ans = 0
# if dp[N] > dp[N-1]:
#     ans = dp[N]
# else:
#     ans = dp[N-1]
print(dp[N])
