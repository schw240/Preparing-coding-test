# N개의 물건 버틸수있는 무게 K,
# 각 물건의 무게 W 물건의 가치 V
N, K = map(int, input().split())
weight = [0]
value = [0]
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)


dp = [[0 for i in range(K+1)] for k in range(N+1)]
for w in range(1, N+1):

    for i in range(1, K+1):
        if i >= weight[w]:

            dp[w][i] = max(dp[w-1][i], dp[w-1][i-weight[w]]+value[w])
        else:

            dp[w][i] = dp[w-1][i]
print(dp[N][K])
