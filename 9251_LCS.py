a = input()
b = input()
dp = [[0]*(len(b)+1) for i in range(len(a)+1)]
#print(dp)

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        # dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + (a[j-1]==b[i-1]))
        # #print(a[j-1] == b[i-1])
        # #print(dp)
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[len(a)][len(b)])