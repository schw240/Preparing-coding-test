# N개의 여행지, 여행 계획에 속한 도시의 수 M
N, M = map(int, input().split(' '))

# 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다.
# 이떄 여행지가 연결되어있다면 양방향으로 이동 가능하다는 의미
# 하나의 여행 계획을 세운 후 이 여행 계획이 가능한지 여부를 판단하고자함

parent = [0] * (N + 1)

# 서로소 집합 알고리즘


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 부모테이블 초기화
for i in range(1, N + 1):
    parent[i] = i

# N줄에 걸쳐 NXN행렬을 통해 임의의 여행지가 연결되어있는지 여부 주어짐 연결되면 1, 아니면 0
for i in range(N):
    # 이게 서로소연산
    graph = list(map(int, input().split()))
    for j in range(N):
        if graph[j] == 1:
            union_parent(parent, i+1, j+1)

# 마지막에 여행계획에 포함된 여행지의 번호들이 주어짐
sites = list(map(int, input().split()))

for i in range(M-1):
    # index? 도시수M 4 0,1 / 1,2 / 2,3 / 3,4
    if find_parent(parent, sites[i]) == find_parent(parent, sites[i+1]):
        res = True
    else:
        res = False

# 출력으로 여행계획이 가능하면 YES, 아니면 No
if res:
    print("YES")
else:
    print("NO")
