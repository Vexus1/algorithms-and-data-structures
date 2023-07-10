#reprezentacja wierzchołka grafu
class Vertex:
    def __init__(self,key):
        ''' Powołanie instancji klasy Vertex, informacja przechowywana jest w kluczu- identyfikatorze danego wierzchołka oraz w liście sąsiedztwa elementów'''
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        ''' Dodaje nowy obiekt do sąsiedztwa wierzchołka'''
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
        

class Graph:
    def __init__(self):
        self.list_of_vertices = {}
        self.num_of_vertices = 0
        self.list_of_edges = []

    def addVertex(self, key):
        new = Vertex(key)
        self.list_of_vertices[key] = new
        self.num_of_vertices += 1
        return new
    
    def getVertices(self, n):
        for i in range(n):
            return self.list_of_vertices[n]
        else: return None 
    
    def contains(self, n):
        return n in self.list_of_vertices

    def add_edge(self,f,t,cost=0):
        if f not in self.list_of_vertices:
            nv = self.addVertex(f)
        if t not in self.list_of_vertices:
            nv = self.addVertex(t)
        self.list_of_vertices[f].addNeighbor(self.list_of_vertices[t], cost)
        edge = f, t
        self.list_of_edges.append(edge)
        return edge
    def display_vertices(self):
        return self.list_of_vertices.keys()
    def display_edges(self):
        return self.list_of_edges
    ### Dodanie metody przepisującej nasze krawędzi grafu na język dot ###
    def convert_to_dot(self):
        sorted_list = sorted(self.list_of_edges)
        dot_lan_code = ""
        for i in sorted_list:
            dot_lan_code = dot_lan_code + '{} -> {} '.format(str(i[0]),str(i[1]))
        digraph = "digraph G {}".format(dot_lan_code)
        return digraph
    def iter(self):
        return iter(self.list_of_vertices.values())


#Wywołanie 
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(1, 4)
graph.add_edge(6, 7)
graph.add_edge(5, 8)
graph.add_edge(6, 8)
graph.add_edge(8, 9)
graph.add_edge(2, 9)

print(graph.convert_to_dot())