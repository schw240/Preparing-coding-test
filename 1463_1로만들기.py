N = int(input())

dp = [0 for _ in range(N+1)]

#N을 받고나서 
#3으로 나누어 떨어지면 3으로 나눈다
#2로 나누어 떨어지면 2로 나눈다
#아니면 1을 뺀다.

#0 0
#1 1
#2 1
#3 1
#4 2
#5 3
#6 2

dp[0] = 0
dp[1] = 0

for i in range(2,N+1):

    dp[i] = dp[i-1] + 1    
    if i%2==0:
        dp[i] = min(dp[i],dp[i//2] + 1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3] + 1)


print(dp[N])