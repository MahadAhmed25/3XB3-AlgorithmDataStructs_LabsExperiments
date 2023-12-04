import SPAlgorithm
import Final_lab.min_heap2 as mh

class A_Star(SPAlgorithm):
    def __init__(self):
        super().__init__()
    
    def calc_sp(self, G, source, destination):
        return self.a_star(G, source, destination, G.get_heuristic())
        
    def a_star(self, G, source, destination, h):
        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        Q = mh.MinHeap([])
        nodes = list(G.adj.keys())

        #Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(mh.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        #Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            
            if current_node == destination: break
            
            for neighbour in G.adj[current_node]:
                g_score = dist[current_node] + G.w(current_node, neighbour)
                if g_score < dist[neighbour]:
                    f_score = g_score + h[neighbour]  # total cost: g_score + heuristic
                    Q.decrease_key(neighbour, f_score)
                    dist[neighbour] = g_score
                    pred[neighbour] = current_node

        # Returning the 2 tuple
        return pred, dist[destination]
            