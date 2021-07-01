N = int(input())
lines = []
dp = [1] * (N + 1)
for i in range(N):
    A, B = map(int, input().split(' '))
    lines.append((A, B))

lines.sort()
print(lines)

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
