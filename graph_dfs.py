# graph traversal(DFS)

graph = {
    1 : [2,3],
    2 : [4,5],
    3 : [6],
    4 : [],
    5 : [6],
    6 : []
    }
visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(visited, graph, i)
dfs(visited, graph, 1)
