"""
입력
N, L(인구차이 L명 이상), R(인구 차이 R명 이하)


출력
인구 이동이 몇번 발생하는지?
"""

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(row, col):
    q = deque()
    q.append([row, col])

    tmp = []
    tmp.append([row, col])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    # 인구차이 안에 있다면 국경선 오픈
                    if L <= abs(A[nx][ny] - A[x][y]) <= R:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        tmp.append([nx, ny])
    return tmp


cnt = 0
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                # 인구 배치가 이뤄져야 하는 나라 tmp
                tmp = bfs(i, j)
                # print(tmp)

                if len(tmp) > 1:
                    flag = True
                    num = sum([A[x][y] for x, y in tmp]) // len(tmp)

                    for x, y in tmp:
                        A[x][y] = num
    if not flag:
        break
    cnt += 1


print(cnt)
