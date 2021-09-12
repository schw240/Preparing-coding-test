# 정사각형으로 이루어진 NXM 크기의 직사각형으로 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 동서남북 중 한곳을 바라본다.
# 맵의 각 칸은 (A, B)로 나타낼 수 있고 A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수
# 캐릭터는 상하좌우로 움직수 있고, 바다로 되어있는 공간에는 갈 수 없다.

# 메뉴얼에 따라 캐릭터를 이동시킨 다음 캐릭터가 방문한 칸의 수를 출력하기

N, M = map(int, input().split(' '))

visited = [[0] * M for _ in range(N)]  # map

# 현재 캐릭터 위치
x, y, d = map(int, input().split(' '))
visited[x][y] = 1

maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
turn = 0


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if maps[nx][ny] == 0 and visited[nx][ny] == 0:
        maps[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn = 0
        continue

    else:
        turn += 1

    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[y]

        if maps[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break

        turn = 0

print(cnt)
