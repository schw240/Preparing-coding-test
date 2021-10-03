import heapq

INF = int(1e9)

# 도시의 개수 N, 통로의 개수 M, 메세지를 보내고자 하는 도시 C
N, M, C = map(int, input().split(' '))
graph = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)

for i in range(M):
    # 통로에 대한 정보 X, Y, Z
    X, Y, Z = map(int, input().split(' '))
    graph[X].append((Y, Z))

q = []
heapq.heappush(q, (0, C))
dist[C] = 0

while q:
    d, cur = heapq.heappop(q)
    if dist[cur] < d:
        continue

    for i in graph[cur]:
        cost = d + i[1]

        if cost < dist[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt = 0
max_d = 0

for d in dist:
    if d != INF:
        cnt += 1
        max_d = max(d, max_d)

print(cnt - 1, max_d)
