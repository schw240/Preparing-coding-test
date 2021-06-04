T = int(input())

dp0 = [0 for _ in range(41)]
dp1 = [0 for _ in range(41)]

dp0[0] = 1
dp1[1] = 1

# fibo(0) = [1, 0]
# fibo(1) = [0, 1]
# fibo(2) = fibo(1) + fibo(0) = [1, 1]
# fibo(3) = fibo(2) + fibo(1) = fibo(1) + fibo(0) + fibo(1) = [1, 2]
# fibo(4) = fibo(3) + fibo(2) = [2, 3]
# dp[n] = dp[n-1] + dp[n-2]

for i in range(2, 41):
    dp0[i] = dp0[i-1] + dp0[i-2]
    dp1[i] = dp1[i-1] + dp1[i-2]

for i in range(T):
    N = int(input())

    print("{} {}".format(dp0[N], dp1[N]))
