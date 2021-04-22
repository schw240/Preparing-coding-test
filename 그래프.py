# BFS와 DFS(그래프에서의 탐색)

"""
대표적인 그래프 탐색 알고리즘
- 너비 우선 탐색(Breadth First Search): 정점들과 같은 레벨에 있는 노드들을 먼저 탐색
- 깊이 우선 탐색(Depth First Search): 정점의 자식들을 먼저 탐색하는 방식
"""

# 파이썬에서 그래프를 표현하는 방법
# 파이썬에서 제공하는 딕셔너리와 리스트 자료구조를 활용하여 그래프 표현하기
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


def dfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


#print(bfs(graph, 'A'))
print(dfs(graph, 'A'))
