class ShortPathFinder:
    def __init__(self):
        self.graph = None
        self.algorithm = None
        
    def set_graph(self, graph):
        self.graph = graph
        
    def calc_short_path(self, source, destination):
        return self.algorithm.calc_sp(self.graph, source, destination)
    
    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    
        