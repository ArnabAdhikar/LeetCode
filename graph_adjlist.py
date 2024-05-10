# graph(adjacency list)

class Graph:
    def __init__(self, size):
        self.sze = size
        self.graph = {}
    def add_vertex(self, v):
        self.graph[v] = []
    def add_edges(self, v1, v2, e):
        '''v1-> vertex 1
        v2-> vertex 2
        e-> weight'''
        temp = [v2, e]
        self.graph[v1].append(temp)
    def del_edges(self, v1, v2):
        self.graph[v1].pop(0)
    def print_graph(self):
        self.graph
        for i in self.graph:
            for j in self.graph[i]:
                print(i, ' -> ', j[0], ' edge weight: ', j[1])

gr = Graph(4)
# add vertex
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)
gr.add_vertex(4)
# add edges
gr.add_edges(1, 2, 1)
gr.add_edges(1, 3, 1)
gr.add_edges(2, 3, 3)
gr.add_edges(3, 4, 4)
gr.add_edges(4, 1, 5)
gr.print_graph()
print(gr.graph)
