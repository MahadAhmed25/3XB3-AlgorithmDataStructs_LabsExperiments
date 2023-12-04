import SPAlgorithm
import Final_lab.min_heap2 as mh

class Bellman_Ford(SPAlgorithm):
    def __init__(self):
        super().__init__()
    
    def calc_sp(self, G, source, destination):
            pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
            dist = {} #Distance dictionary
            nodes = list(G.adj.keys())

            num_dec =0 
            

            #Initialize distances
            for node in nodes:
                dist[node] = float("inf")
            dist[source] = 0
            num_dec=num_dec+1

            #Meat of the algorithm
            for _ in range(G.number_of_nodes()):
                for node in nodes:
                    for neighbour in G.adj[node]:
                        if dist[neighbour] > dist[node] + G.w(node, neighbour):
                            dist[neighbour] = dist[node] + G.w(node, neighbour)
                            pred[neighbour] = node
                            num_dec = num_dec + 1
                            if neighbour == destination:
                                return dist
                            
            return dist
