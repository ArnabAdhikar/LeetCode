# Course Schedule II
"""
Created on Mon Feb  5 20:33:24 2024

@author: ARNAB ADHIKARY
"""

class Solution:
    def findOrder(self, n: int, prerequisites):
        # bulding the adjacency list
        prereq = {c:[] for c in range(n)}
        for i, j in prerequisites:
            prereq[i].append(j)
        # cycle check
        output = []
        visit = set()
        cycle = set()
        def cyclecheck(vertex):
            if vertex in cycle:
                return False
            if vertex in visit:
                return True
            # checking if there is any cycle
            cycle.add(vertex)
            for i in prereq[vertex]:
                if cyclecheck(i) == False:
                    return False
            # vertex dont have any cycle
            cycle.remove(vertex)
            visit.add(vertex)
            output.append(vertex)
            return True
        # Runner Code
        for course in range(n):
            if cyclecheck(course) == False:
                return []
        return output
