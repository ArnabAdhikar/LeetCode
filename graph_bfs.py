# graph traversal(BFS)
# queue

graph = {
    1 : [2,3],
    2 : [4,5],
    3 : [6],
    4 : [],
    5 : [6],
    6 : []
    }
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
bfs(visited, graph, 1)
