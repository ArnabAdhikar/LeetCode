# Find Eventual Safe States

class Solution:
    def eventualSafeNodes(self, graph):
        # DFS
        n = len(graph)
        hashmap = {}
        def dfs(node):
            # we already determined whether the node is safe or not
            if node in hashmap:
                return hashmap[node]
            # if we dont know
            hashmap[node]=False
            for neighbour in graph[node]:
                # if 1 of the neighbour is not a safe node, the current 
                # node is also not safe
                if not dfs(neighbour):
                    return False
            hashmap[node] = True
            return True
        # DFS determines whether this node is a safe node
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans