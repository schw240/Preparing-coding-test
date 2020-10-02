#N 종류 합 K
N, K = map(int, input().split())
sum = 0

money = [int(input()) for i in range(N)]

for i in range(1,N+1):
    coin = money[-i]
    if K >= coin:
        tmp = K//coin
        K -= coin * tmp
        sum += tmp
        #print(sum, K, tmp, coin)

print(sum)