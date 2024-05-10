# https://leetcode.com/problems/redundant-connection/
# union Find Problem

from typing import List
class Solution:
    def findRedundantConnection(self, edges) -> List[int]:
        # initializing the parent and the rank
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        def find(node):
            # initial parent
            p = parent[node]
            # finding the last root parent
            while p!=parent[p]:
                # link compression
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(node1, node2):
            # finding the parent of 2 nodes
            p1, p2 = find(node1), find(node2)
            if p1==p2:
                # same parent cycle encountered
                return False
            # unioning them
            if rank[p1] > rank[p2]:
                # p1 is the parent of p2
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        # Driver code
        for n1, n2 in edges:
            if union(n1,n2)==False:
                return [n1,n2]
