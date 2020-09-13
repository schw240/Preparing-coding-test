def change(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2

def find(r,c,d):
    cnt = 1
    x = r
    y = c
    arr[x][y] = 2 
    while(True):
        dc = d
        for i in range(4):
            empty = 0
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]
            if(0<=nx<n and 0<=ny<m and arr[nx][ny] == 0):
                cnt += 1
                x = nx
                y = ny
                arr[nx][ny] = 2
                d = dc
                empty = 1
                break
        # 4방향 탐색 + 모든 칸이 청소
        if(empty == 0):
            # 후진
            if(d == 0):
                x += 1
            elif(d == 1):
                y -= 1
            elif(d == 2):
                x -= 1
            elif(d == 3):
                y += 1
            #벽인경우 후진
            if(arr[x][y] == 1):
                break
    return cnt
#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
#좌표(r,c),방향
r, c, d = map(int, input().split())
#지도
arr = [list(map(int, input().split())) for i in range(n)]
res = find(r,c,d)
print(res)