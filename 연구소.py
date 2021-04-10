# 세로 N 가로 M
# N개 줄에 지도의 모양
# 0은 빈칸, 1은 벽, 2는 바이러스
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기

import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()

