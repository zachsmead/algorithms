class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = []

		self.distance = 9999
		self.color = 'black'

	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()




class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices: # if the input is actually a vertex
																																				# and not already in the list of this
																																				# graph's vertices
			self.vertices[vertex.name] = vertex # add this vertex to the list of vertices, designated by its name.
			# print self.vertices
			return True
		else:
			return False

	def add_edge(self, u, v): # u and v denote the names of the vertices, i.e. the keys in self.vertices
		if u in self.vertices and v in self.vertices: # if both vertices are in the graph, add them to
																																# ea.o as neighbors
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())): # second term calls a list of keys (names) from self.vertices
			print (key + str(self.vertices[key].neighbors) + ' ' + str(self.vertices[key].distance))

	def breadth_first_search(self, vertex):
		queue = []
		vertex.distance = 0
		vertex.color = 'red'
		for v in vertex.neighbors:
			self.vertices[v].distance = vertex.distance + 1
			queue.append(v)

		while len(queue) > 0:
			u = queue.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red'

			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color =='black':
					queue.append(v)
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1

g = Graph()
# a = Vertex('A')
# g.add_vertex(a)
# g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')): # use a loop to populate the graph with vertices
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.breadth_first_search(a)

g.print_graph()


