class Vertex:
	def init(self, n):
		self.name = n
		self.neighbors = []

		self.distance = 9999
		self.color = 'black'

	def add_neighbors(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices: # if the input is actually a vertex
																																				# and not already one of this graph's
																																				# vertices
			self.vertices[vertex.name] = vertex # add this vertex to the list of vertices, designated by its name.




def breadth_first_search():
	pass


