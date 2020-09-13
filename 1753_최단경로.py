import heapq

#정점, 간선
v, e = map(int, input().split())
start = int(input())

# 인접리스트
adj = {i: [] for i in range(1, v+1)}
for _ in range(e):
    s, e, w = map(int, input().split())
    # 방향 그래프
    adj[s].append([e, w])

INF = float('inf')
#가중치 담을 배열
dist = [INF] * (v + 1)

# 힙큐로 최소값 리턴
hq = []
heapq.heappush(hq, (0, start))
dist[start] = 0

while hq:
    # 가중치, 노드
    k, u = heapq.heappop(hq)
    for w, cost in adj[u]:
        # 현재 가중치와 다른경로로 가는 가중치 비교
        if cost + dist[u] < dist[w]:
            # 가중치를 더 작은 것으로 업데이트, 힙큐에 저장
            dist[w] = cost + dist[u]
            heapq.heappush(hq, (dist[w], w))

for i in range(1, v+1):
    if dist[i] != INF:
        print(dist[i])
    else:
        print('INF')