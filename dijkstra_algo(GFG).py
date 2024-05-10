# dijakstra algorithm
# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
"""
Created on Tue Feb  6 22:33:57 2024

@author: ARNAB ADHIKARY
"""

from collections import deque
class Solution:
    def dijkstra(self, V, adj, S):
        #code here
        dis = [float("inf") for i in range(V)]
        q = deque([])
        # queue stores the distance and the node
        q.append([0,S])
        dis[S]=0
        # BFS
        while q:
            cur = q.popleft()
            node = cur[-1]
            cur_dis = cur[0]
            # traversing the adjacency list
            for i in adj[node]:
                # weight between the connection
                node_weight = i[-1]
                # actual node
                adj_node = i[0]
                if (cur_dis + node_weight < dis[adj_node]):
                    dis[adj_node] = cur_dis + node_weight
                    q.append([cur_dis + node_weight , adj_node])
        return dis

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
