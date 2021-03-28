# 볼링공 개수 N개 볼링공 무게 1부터 M까지

N, M = map(int, input().split())
ball_weight = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        if ball_weight[i] != ball_weight[j]:
            cnt += 1
print(cnt)
