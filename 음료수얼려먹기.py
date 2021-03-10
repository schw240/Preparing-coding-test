# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        print("북")
        dfs(x, y - 1)
        print("서")
        dfs(x + 1, y)
        print("남")
        dfs(x, y + 1)
        print("동")
        return True
    return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 모든 노드 위치에 대하여 음료수ㅜ 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            print(i, j, "i, j")
            result += 1

print(result)
