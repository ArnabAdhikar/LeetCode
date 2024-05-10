class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        def find(node: int)-> int:

            if node == par[node]: return node
            par[node] = find(par[node])
            return par[node]

        def union(u: int, v: int, w: int)-> int:

            x, y  = find(u), find(v)
            wgt[y]&= wgt[x] & w
            par[x] = y

        def findwgt(query: list)-> int:

            s, t = query
            if s == t: return 0
            if find(s)!=find(t): return -1
            return wgt[find(s)]
        

        par, ans = list(range(n)), []
        wgt = [(1<<31)-1] * n

        for edge in edges: union(*edge)
            
        return map(findwgt, queries)