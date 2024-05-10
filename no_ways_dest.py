# no of ways to arrive at destination

# dijakstra algo.
import heapq
from collections import defaultdict 
class Solution:
    def countPaths(self, n: int, roads) -> int:
        # creating the adjacency list
        adj_list = defaultdict(list)
        for i,j,k in roads:
            adj_list[i].append((j,k))
            adj_list[j].append((i,k))
        # defining the starting point and the ending point
        start = 0
        till = n-1
        # set minimum distance of all nodes but start to infinity.
        min_dist = {i:[float('inf'),0] for i in adj_list.keys()}
        # min_dist[i] = [minimum time from start, number of ways to get to node i in min time]
        min_dist[start] = [0,1]
        # declaring the heap initialized with initial values
        # Heap nodes in the format (elapsed time to get to that node, node index)
        heap = [(0, start)]
        while heap:
            time, node = heapq.heappop(heap)
            # if nodes getting popped have a higher elapsed time than minimum time required
            # to reach end node(time elapsed cannot be negetive) or Edge case
            if min_dist[till][0] < time:
                break
            for neigh, t in adj_list[node]:
                if (t+time) > min_dist[neigh][0]:
                    continue
                # if time is equal to minimum time to node, add the ways
                elif (t + time) == min_dist[neigh][0]:
                    min_dist[neigh][1] = min_dist[neigh][1] + min_dist[node][1]
                # node has not been visited before. Set minimum time and the ways
                else:
                    min_dist[neigh][0] = time + t
                    min_dist[neigh][1] = min_dist[node][1]
                    heapq.heappush(heap, (time + t,neigh))
        return min_dist[till][1]%(pow(10,9)+7)
