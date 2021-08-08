import heapq

INF = 1000000

N, M = map(int, input().split(' '))

# 첫번쨰는 숨어야하는 헛간의 번호(거리가 같은 헛간이 여러개면 가장 작은 헛간 번호)
# 두번쨰는 헛간까지의 거리, 세번째는 그 헛간과 같은 거리를 갖는 헛간의 개수 출력하기

start = 1
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

# 간선정보 입력받기
for i in range(M):
    A, B = map(int, input().split(' '))
    graph[A].append((B, 1))
    graph[B].append((A, 1))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    # 이미 처리된적이 있다는 의미
    if distance[now] < dist:
        continue

    # 현재 노드와 인접한 노드 확인과정
    for node in graph[now]:
        # dist + 인접노드
        cost = dist + node[1]

        if cost < distance[node[0]]:
            distance[node[0]] = cost
            heapq.heappush(q, (cost, node[0]))

max_node = 0
max_distance = 0

res = []

for i in range(1, N+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        res = [max_node]
    elif max_distance == distance[i]:
        res.append(i)

print(max_node, max_distance, len(res))
