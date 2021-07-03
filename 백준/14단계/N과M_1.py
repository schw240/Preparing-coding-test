N, M = map(int, input().split(' '))
visited = [False] * N
res = []


def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1, N+1):
        if i not in res:
            res.append(i)
            dfs()
