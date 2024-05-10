# Shortest path in Undirected Graph having unit distance
"""
Created on Tue Feb  6 20:57:55 2024

@author: ARNAB ADHIKARY
"""

#User function Template for python3
from collections import deque
class Solution:
    # creating the adjacent list
    @staticmethod
    def generate_adj_list(edges, v):
        adj = [[] for _ in range(v)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        return adj
    
    def shortestPath(self, edges, n, m, src):
        # n: no of nodes; m: no of edges; src: input parameter/ source
        visited = set()
        dist = [-1]*n
        # distance between source to source
        dist[src] = 0
        q = deque()
        # initially source is already visited
        q.append(src)
        visited.add(src)
        # generate the adjacency list for edges and vertices
        adj = self.generate_adj_list(edges, n)
        # BFS
        while q:
            # now is the node
            now = q.popleft()
            for i in adj[now]:
                # the node has not been visited
                if i not in visited:
                    dist[i] = dist[now]+1
                    visited.add(i)
                    q.append(i)
        return dist
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
