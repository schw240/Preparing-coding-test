from itertools import combinations



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#0 빈칸 1집 2치킨집
#1<집 개수<2N // M<=치킨집=<13 
house = []
chicken =[]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i+1,j+1))
        elif board[i][j] == 2:
            chicken.append((i+1,j+1))

#print(house[0])
#print(type(house[0]))

#폐업시키지 않을 치킨집 최대 M개를 골랐을때 도시의 치킨 거리의 최소값구하기
#(r1,c1) (r2,c2) => abs(r1-r2) + (c1+c2)

#전체 치킨집중 M개를 선택하되 그중에서 거리가 최소가 되는곳
min_val = float('inf')

for ch in combinations(chicken, M):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
    if sumv < min_val:
        min_val = sumv

print(min_val)