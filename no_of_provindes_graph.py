# No of provinces(adjacency matrix) in agraph

class Solution:
    def findCircleNum(self, isConnected) -> int:
        visited = set()
        c = 0
        # dfs is performed on an individual list present in the adj list
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                # calling DFS only when, isConnected[start][end]==1 and end not in visited
                if isConnected[start][end] and end not in visited:
                    dfs(end)
        # traversing through the nested matrix
        for i in range (len(isConnected)):
            if i not in visited:
                # starting of the new province as i is not visited till now
                c+=1
                dfs(i)
        return c
    