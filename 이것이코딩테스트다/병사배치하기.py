N = int(input())
scores = list(map(int, input().split(' ')))
scores.reverse()

# 병사를 배치할 때 전투력이 높은 병사가 앞으로 오도록 내림차순 배치
# 이때 정렬을 쓰는게 아니라 열외를 쓰는 방법으로 배치

dp = [1] * N

# 남아있는 병사의 수가 최대가 되도록 하기 위해 열외시켜야 하는 병사의 수
for i in range(1, N):
    for j in range(i):
        if scores[j] < scores[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
