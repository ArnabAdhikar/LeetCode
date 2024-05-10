# creating a graph.
class Graph:
	def __init__(self):
		self.lst = {}
	def print_g(self):
		for i in self.lst:
			print(i," : ",self.lst[i])
	# adding a vertex
	def vertex(self, val):
		if val not in self.lst.keys():
			self.lst[val]=[]
			return True
		return False
	# adding an edge
	def edge_a(self,v1,v2):
		if v1 in self.lst.keys() and v2 in self.lst.keys():
			self.lst[v1].append(v2)
			self.lst[v2].append(v1)
			return True
		return False
	# removing an edge
	def edge_d(self,v1,v2):
		if v1 in self.lst.keys() and v2 in self.lst.keys():
			try:
				self.lst[v1].remove(v2)
				self.lst[v2].remove(v1)
				return True
			except:
				print("This value has no vertex.")
		return False
	# removing a vertex.
	def vert_re(self,vertex):
		if vertex in self.lst.keys():
			for i in self.lst[vertex]:
				self.lst[i].remove(vertex)
			del self.lst[vertex]
			return True
		return False
g = Graph()
g.vertex("A")
g.vertex("B")
g.vertex("C")
g.vertex("D")
g.edge_a("A","B")
g.edge_a("B","C")
g.edge_a("C","A")
g.print_g()
g.edge_d("A","D")
g.print_g()
g.vert_re("D")
g.print_g()
