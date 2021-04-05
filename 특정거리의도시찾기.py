import sys
from collections import deque

input = sys.stdin.readline

# 도시개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
visited[x] = 0

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

q = deque([x])

while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v] + 1
            q.append(i)

for i in range(n+1):
    if visited[i] == k:
        print(i)
if k not in visited:
    print(-1)
