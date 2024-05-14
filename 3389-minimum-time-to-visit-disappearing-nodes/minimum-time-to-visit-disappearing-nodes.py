class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, length in edges:
            adj[u].append((v, length))
            adj[v].append((u, length))

        pq = [(0, 0)]  # (cost, node)
        res = [-1 for _ in range(n)]
        while pq:
            current_time, u = heapq.heappop(pq)
            if res[u]!=-1:
                continue
            res[u]=current_time
            for v, length in adj[u]:
                if res[v]!=-1:
                    continue
                travel_time = current_time + length
                if travel_time<disappear[v]:
                    heapq.heappush(pq, (travel_time, v))

        return res