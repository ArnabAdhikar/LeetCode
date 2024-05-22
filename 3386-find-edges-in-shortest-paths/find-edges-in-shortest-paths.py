class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges: 
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def fn(source): 
            dist = [inf]*n
            dist[source] = 0 
            pq = [(0, source)]
            while pq: 
                x, u = heappop(pq)
                if dist[u] == x: 
                    for v, w in graph[u]: 
                        if x+w < dist[v]: 
                            dist[v] = x+w
                            heappush(pq, (x+w, v))
            return dist 
        
        dist0, dist1 = fn(0), fn(n-1)
        return [dist0[n-1] < inf and (dist0[u] + w + dist1[v] == dist0[n-1] or dist0[v] + w + dist1[u] == dist0[n-1]) for u, v, w in edges]
