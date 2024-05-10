# Network Delay Time

import collections
import heapq
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        # building up the adjacency list
        edges = collections.defaultdict(list)
        # u:starting, v:ending, w:weight
        for u, v, w in times:
            edges[u].append((v, w))
        # Dijakstra(BFS)
        # minheap: initial distance and the starting vertex
        minheap = [(0, k)]
        visited = set()
        result = 0
        while minheap:
            # w1: Weight, n1: node
            w1, n1 = heapq.heappop(minheap)
            # if the node is already visited
            if n1 in visited:
                continue
            visited.add(n1)
            result = max(result, w1)
            # BFS
            # n2: neighbouring node, w2: weight of the node
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    # total path taken to reach the neighbouring node through the 
                    # master node = w1+w2
                    heapq.heappush(minheap, (w1+w2, n2))
        if len(visited)==n:
            return result
        else:
            return -1
