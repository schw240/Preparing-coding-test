# 여행가 A는 NXN 정사각형 공간위에 서 있다.
# L, R, U D가 들어오는데 좌우,상하로 1칸씩 이동
# A가 NXN 크기 정사각형 공간을 벗어나는 움직임은 무시됨

N = int(input())  # 공간크기
plans = list(map(str, input().split(' ')))
x, y = 1, 1


for i in range(len(plans)):

    if(plans[i] == 'L'):
        nx = x
        ny = y - 1
    elif(plans[i] == 'R'):
        nx = x
        ny = y + 1
    elif(plans[i] == 'U'):
        nx = x - 1
        ny = y
    else:
        nx = x + 1
        ny = y

    if(nx < 1 or ny < 1 or nx > N or ny > N):
        continue

    x, y = nx, ny

print(x, y)
