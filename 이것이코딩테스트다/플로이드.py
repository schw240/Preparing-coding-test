# 하나의 정점에서 다른 정점으로 갈 수 있으면 최소비용,갈수없으면 INF
# 3중 for문을 이용해 각 정점을 확인하며 값 변경
# 위 과정을 반복해 모든 정점 사이 최단 경로 탐색

# n개의 도시, m개의 버스
n = int(input())
m = int(input())
inf = 100000000
s = [[inf] * n for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if s[a - 1][b - 1] > c:
        s[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

for i in s:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
