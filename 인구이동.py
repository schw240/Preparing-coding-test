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
A = [list(map(int, input().spli())) for _ in range(N)]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    move_q = deque()
    q.append([x, y])
    c[x][y] = 1
    people, cnt = 0, 0
    while q:
        x, y = q.popleft()
        move_q.append([x, y])
        people += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not c[nx][ny]:


def bfs(row, col):


def move():
    # 인구이동
    cnt, pre_cnt = 0, 0
    while True:
        is_Move = False
        total_visited = set()
        temp = []

        for i in range(N):
            for j in range(N):
                if (i, j) not in total_visited:


print(move())
