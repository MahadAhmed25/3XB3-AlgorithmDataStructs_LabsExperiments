
from Graph import *
from SPAlgorithm import *

class ShortPathFinder:
    
    def __init__(self):
        self.graph = None
        self.algorithm = None
        
    def set_graph(self, graph):
        self.graph = graph
        
    def calc_short_path(self, source, dest):
        return self.algorithm.calc_sp(self.graph, source, dest)
    
    def set_algorithm(self, algorithm):
        self.algorithm = algorithm
        
        

#TESTING
a = ShortPathFinder()
G = WeightedGraph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2,1)
G.add_edge(2,3,1)

a.set_graph(G)
a.set_algorithm(A_Star())
m = a.calc_short_path(1, 3)
print(m)
    
        