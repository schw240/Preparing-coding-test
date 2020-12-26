#오름차순을 이루는 수
#인접한 수가 같아도 오름차순
#dp[N][i] = sum(dp[N-1][i]~dp[N-1][9])

N = int(input())
dp = [[0]*10 for i in range(3)]
for i in range(10):
    dp[1][i] = 1
    dp[2][i] = 10 - i

for i in range(3, N+1):
    tmp = [0] * 10
    for j in range(10):
        if j == 9:
            tmp[j] = 1
        else:
            tmp[j] = sum(dp[i-1][j:])%10007
    dp.append(tmp)

print(sum(dp[N]) % 10007)