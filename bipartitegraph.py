from collections import deque
class Solution:
    def isBipartite(self, graph) -> bool:
        color=[-1]*len(graph)
        def bfs(start,graph,color):
            # sample color = 0,1
            q=deque()
            # let the first element be coloured as 0
            color[start]=0
            q.append(start)
            # traversing the queue
            while(len(q)!=0):
                element=q.popleft()
                for ele in graph[element]:
                    # if the neighbouring node is not coloured
                    if(color[ele]==-1):
                        # colouring with the alternate colour
                        if(color[element]==0):
                            color[ele]=1
                            # we visited the neighbouring node
                            q.append(ele)
                        else:
                            color[ele]=0
                            q.append(ele)
                    else:
                        # if any one consecutive element has the same colour-> Non- Bipartite
                        # checking from the colour array
                        if(color[ele]==color[element]):
                            return False 
            return True
        for i in range(len(graph)):
            # the node is not coloured
            if (color[i]==-1) and (bfs(i, graph, color)==False):
                return False
        return True
