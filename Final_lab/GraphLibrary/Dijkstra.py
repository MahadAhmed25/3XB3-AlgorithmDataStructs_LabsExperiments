import SPAlgorithm
import Final_lab.min_heap2 as mh

class Dijsktra(SPAlgorithm):
    
    def __init__(self):
        super().__init__()
    
    def calc_sp(self, G, source, destination):
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        Q = mh.MinHeap([])
        nodes = list(G.adj.keys())
        sum = 0

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(mh.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)
        sum += 1

        # Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key

            if current_node == destination:
                # Reached the destination, construct and return the path
                path = []
                current_node = destination
                while current_node in pred:
                    path.insert(0, current_node)
                    current_node = pred[current_node]
                # Include the source node in the path
                path.insert(0, source)
                #print(path)
                return path

            for neighbour in G.adj[current_node]:
                if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    sum += 1
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
                    
        # If destination is not reached, return an empty path
        return []