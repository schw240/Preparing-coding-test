n = int(input())
wine = [0]
dp = [0] * (n+1)
for i in range(1,n+1):
    wine.append(int(input()))
#print(wine)

#print(dp)
for i in range(1, n+1):
    if i == 1:
        dp[1] = wine[1]
    elif i == 2:
        dp[2] = wine[1] + wine[2]
    else:
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    #print(dp)

print(dp[n])

