N, M = map(int, input().split(' '))  # 회사의 개수 N, 경로의 개수 M

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] == 0

for i in range(M):
    # 연결된 두 회사의 번호
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1

# M+2 번줄 X와 K가 공백으로 주어짐 X번 회사에 방문하여 배달전 K번 회사에 상대에게 소개팅
# 1번회사에서 출발하여 K번 회사 방문 뒤 X번 회사로 가는 길 중 가장 빠르게 이동

x, k = map(int, input().split())

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = graph[1][k] + graph[k][x]

if ans >= INF:
    print("-1")
else:
    print(ans)
