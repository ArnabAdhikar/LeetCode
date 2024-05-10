# topological sort

def dfs(node, visited, stack, adj):
    visited[node] = True
    for j in adj[node]:
        if not visited[j]:
            dfs(j, visited, stack, adj)
        # after every DFS traversal push the node into the stack
        stack.append(node)
def topologicalSort(adj, V, E):
    # Write your code here
    if E==0:
        return []
    visited = [False for i in range(V)]
    stack = []
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack, adj)
    stack.reverse()
    return stack