# Course Schedule

class Solution:
    def build(self, numCourses, prerequisites):
        adj = [[] for i in range(numCourses)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in prerequisites:
            adj[c2].append(c1)
        return adj
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = self.build(numCourses, prerequisites)
        status = [0]*numCourses
        def cyclecheck(vertex):
            if status[vertex] == 1:
                return False
            if status[vertex] == -1:
                return True
            # checking if there is any cycle, return True
            status[vertex] = -1
            for i in adj[vertex]:
                if cyclecheck(i):
                    return True
            # else make the status-> 1 and return False
            status[vertex] = 1
            return False
        # now checking cucles of all the vertex connected to the nodes in list
        for vertex in range(numCourses):
            if cyclecheck(vertex) == True:
                return False
        return True
