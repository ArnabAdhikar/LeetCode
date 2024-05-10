# prims Algo
# https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/1172452319/
# https://www.youtube.com/watch?v=f7JOBJIC-NA

import heapq
class Solution:
    def minCostConnectPoints(self, points) -> int:
        # building the adjacency list
        n = len(points)
        # i:[cost, node]
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1, n):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        # Prim's Algorithm
        total_cost = 0
        visited = set()
        minheap = [[0,0]]
        while len(visited)<n:
            cost, i = heapq.heappop(minheap)
            if i in visited:
                # the node is laready visited so skip
                continue
            total_cost+=cost
            visited.add(i)
            # check for the neighbourers of this node
            for neighnour_cost, neighbour in adj[i]:
                if neighbour not in visited:
                    heapq.heappush(minheap, [neighnour_cost, neighbour])
        return total_cost
