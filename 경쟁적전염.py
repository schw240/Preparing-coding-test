# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식
# 가장 번호가 낮은 종류의 바이러스부터 증식한다.

# 바이러스 종류 K
# S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하세요

from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
viruses = []

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            # 바이러스 숫자, x위치, y위치, 시간
            viruses.append((graph[i][j], i, j, 0))

# print(viruses)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

viruses.sort()
q = deque(viruses)

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, nx, ny, time-1))

print(graph[X-1][Y-1])
