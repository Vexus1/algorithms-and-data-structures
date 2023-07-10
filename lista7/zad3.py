from queue import Queue
import sys

#reprezentacja wierzchołka grafu
class Vertex:
    def __init__(self,key):
        ''' Powołanie instancji klasy Vertex, informacja przechowywana jest w kluczu- identyfikatorze danego wierzchołka oraz w liście sąsiedztwa elementów'''
        self.id = key
        self.connectedTo = {}
        self.color = 'white'      
        self.dist = sys.maxsize    
        self.pred = None          
        self.disc = 0             
        self.fin = 0              

    def addNeighbor(self,nbr,weight=0):
        ''' Dodaje nowy obiekt do sąsiedztwa wierzchołka'''
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

        
#reprezentacja grafu
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


def bfs(g,start):
    """Algorytm przeszukiwania wszerz"""
    start.setDistance(0)                           
    start.setPred(None)                         
    vertQueue = Queue()
    vertQueue.enqueue(start)                      
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()           
        for nbr in currentVert.getConnections():    
            if (nbr.getColor() == 'white'):         
                nbr.setColor('gray')                            
                nbr.setDistance(currentVert.getDistance() + 1)   
                nbr.setPred(currentVert)                         
                vertQueue.enqueue(nbr)                           
        currentVert.setColor('black')           


class DFSGraph(Graph):
    """Algorytm przeszukiwania w głąb"""
    def __init__(self):
        super().__init__()
        self.time = 0
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
