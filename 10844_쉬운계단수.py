N = int(input())

# 1
# 1 2 3 4 5 6 7 8 9
# 2
# 10 12 23 34 45 56 67 78 89 21 32 43 54 65 76 87 98
# 3
# 123 234 345 456 567 678 789 210 321 432 543 654 765 876 987 101 121 212 ..

dp = [[0]*10 for i in range(N+1)]
#print(dp)

for i in range(1,10):
    dp[1][i] = 1
print(dp)

if N == 1:
    print(sum(dp[1]))
else:
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]