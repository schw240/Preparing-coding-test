import heapq

INF = 1000000

N, M = map(int, input().split(' '))

# 첫번쨰는 숨어야하는 헛간의 번호(거리가 같은 헛간이 여러개면 가장 작은 헛간 번호)
# 두번쨰는 헛간까지의 거리, 세번째는 그 헛간과 같은 거리를 갖는 헛간의 개수 출력하기

start = 1
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    A, B = map(int, input().split(' '))
    graph[A].append((B, 1))
    graph[B].append((A, 1))
