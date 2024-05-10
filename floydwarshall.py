# Find the City With the Smallest Number of Neighbors at a Threshold Distance
"""
Created on Fri Feb  9 13:41:35 2024

@author: ARNAB ADHIKARY
"""
# Floyd Warshall algorithm
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        # building up the cost matrix with all the initial valies as infinity
        cost=[[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
        # replacing infinity with the actual distance value diagonally
        for u,v,d in edges:
            cost[u][v]=d
            cost[v][u]=d
        # replacing the cost value with actual cost
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j]=min(cost[i][j],cost[i][via]+cost[via][j])
        # storingthe no of nodes wih cost<=threshold limit
        d={}
        for i in range(n):
            c=0
            for j in range(n):
                if cost[i][j]<=distanceThreshold and i!=j:
                    c+=1
            d[i]=c
        # implementing the last step
        m1 = min(d.values())
        m2 = 0
        for k,v in d.items():
            if m1==v:
                m2 = max(m2, k)
        return m2
