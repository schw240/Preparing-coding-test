#지도 세로 N, 가로 M
#주사위 좌표 x,y
#명령의 개수 K
#동1,서2,북3,남4
#이동할때마다 주사위 윗면에 쓰여있는 수 출력
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))


dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
# 가장 처음에 주사위의 값 0
dice, temp = [0]*6, [0]*6
direction = [
    (2, 0, 5, 3, 4, 1), # 동쪽
    (1, 5, 0, 3, 4, 2), # 서쪽
    (4, 1, 2, 0, 5, 3), # 북쪽
    (3, 1, 2, 5, 0, 4) # 남쪽
]


# 동쪽(오른쪽) 1, 서쪽 2, 북쪽(위쪽) 3, 남쪽 4
for command in commands:
    command -= 1
    x, y = x + dx[command], y + dy[command] # 움직이는 x, y좌표 구한다
    if x < 0 or x >= N or y < 0 or y >= M: # 맵보다 커지지 않도록 제한
        x, y = x - dx[command], y - dy[command]
        continue
    for idx in range(6):
        temp[idx] = dice[idx]
    for idx in range(6):
        dice[idx] = temp[direction[command][idx]]
    if board[x][y]:
        dice[5] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[5]
    print(dice[0])
