# G개의 탑승구가 있고 1번부터 G번까지 구분

# P개의 비행기가 차례대로도착할 예정이며 i번쨰부터 g번째 탑승구 중 하나에 영구적으로 도킹해야한다.
# 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다. - 서로소 집합

# P개의 비행기를 순서대로 도킹하다가 만약 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우
# 그 시점에서 공항의 운행을 중지

# 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 할때 최대 몇대를 도킹할 수 있는지 출력하는 프로그램 작성하기


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


G = int(input())  # 탑승구
P = int(input())  # 비행기

parent = [0 for _ in range(G+1)]

for i in range(1, G+1):
    parent[i] = i

# 최대 비행기 개수
max_cnt = 0

for i in range(P):
    plane = int(input())
    # 현재 비행기의 탑승구 루트 확인
    data = find_parent(parent, plane)

    # 현재 루트가 0이면 종료
    if data == 0:
        break
    # 그렇지 않으면 왼쪽 집합과 합치기
    union_parent(parent, data, data-1)
    max_cnt += 1


print()
print(max_cnt)
