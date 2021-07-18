# 최적의 경로를 찾도록
# [0][0] 위치에서 가장 오른쪽 아래칸인 [N-1][N-1]칸으로 이동하는 최소비용을 출력하기

# 다익스트라 알고리즘
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가능 비용을 계산하여 최단거리 테이블 갱신
# 5. 3,4번 반복

import heapq

INF = 1000000

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for i in range(T):
    N = int(input())

    graph = []

    for j in range(N):
        graph.append(list(map(int, input().split(' '))))

    # 최단거리 테이블
    distance = [[INF] * N for _ in range(N)]

    x, y = 0, 0  # 시작 위치
    # 시작 노드로 가기 위한 비용은(0, 0) 위치의 값으로 설정, 큐 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵의 범위 확인
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            cost = dist + graph[nx][ny]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[N-1][N-1])
