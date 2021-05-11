# 집 N개 수직선, 공유기 C개
N, C = map(int, input().split(' '))
house = []

for i in range(N):
    house.append(int(input()))

house.sort()
# 가장 인접한 두 공유기 사이의 거리를 최대값 탐색
# C개보다 많은 공유기를 설치할 수 있다면 가장 인접한 두 공유기 사이의 거리를 증가시켜
# 더 큰 값에서도 성립하는지 체크
# 1 2 4 8 9
# 최소 gap 1, 최대 gap 8
start = house[1] - house[0]
end = house[-1] - house[0]
cnt = 0

while(start <= end):
    mid = (start + end) // 2
    cnt += 1
    