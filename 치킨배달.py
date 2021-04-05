# 크기 N인 도시
# 각 칸은 빈칸 0, 집 1, 치킨집 2 중 하나
# 도시의 칸은 (r,c)와 같은 형태 r은 행 c는 열 둘다 1부터 시작
# 최대 수익 치킨집 M
# 도시의 치킨거리가 가장 작게 되는지?  도시의 치킨거리 = 모든 집의 치킨 거리의 합
# abs(r1 - r2) + abs(c1 - c2)

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#print(N, M)
# print(board)

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

minv = float('inf')
# 전체 치킨집에서 M개를 선택하고 거리가 가장 최소가 되는 minv로 골라야함
for ch in combinations(chicken, M):  # combinations(list, 개수) 조합 만들어줌
    total = 0
    # print(ch)
    for hx, hy in house:
        total += min([abs(hx - cx) + abs(hy - cy) for cx, cy in ch])

    if total < minv:
        minv = total

print(minv)
