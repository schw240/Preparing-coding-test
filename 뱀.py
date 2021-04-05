from collections import deque

# 보드 크기 N
# 사과의 개수 K


def check(x, y):
    return True if 0 <= x and x < N and 0 <= y and y < N else False


def turn_around(direction):
    global d
    if direction == 'D':
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d


N = int(input())
K = int(input())
board = [[0] * (N) for i in range(N)]

# K 줄 만큼 사과의 위치 첫번째는 행 두번째는 열
for i in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

# 뱀의 방향 변환 횟수 L
# L개의 줄에는 방향 변환 정보 X와 C로 이루어짐
L = int(input())
rotation = {}
for i in range(L):
    X, C = input().split()
    rotation[int(X)] = C

# 뱀 위치
snake = deque([[0, 0]])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음 방향 동쪽으로 가야함
d = 1
times = 0
nx, ny = 0, 0


while True:
    times += 1
    nx += dx[d]
    ny += dy[d]

    if times in rotation.keys():
        d = turn_around(rotation[times])

    if check(nx, ny):
        if [nx, ny] in snake:  # 벽에 부딪히면
            break

        if board[nx][ny] == 1:  # 사과먹고 길이1증가
            board[nx][ny] = 0
            snake.append([nx, ny])

        elif board[nx][ny] == 0:
            snake.append([nx, ny])
            x, y = snake.popleft()
    else:
        break

print(times)
