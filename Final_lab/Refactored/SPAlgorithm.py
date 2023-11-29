import min_heap2

class SPAlgorithm:
    def __init__(self):
        pass
    
    def calc_sp(self, graph, source, dest):
        pass
    
    
class Dijsktra(SPAlgorithm):
    
    def __init__(self):
        super().__init__()
    
    def calc_sp(self, G, source, destination):
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        Q = min_heap2.MinHeap([])
        nodes = list(G.adj.keys())
        sum = 0

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap2.Element(node, float("inf")))
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

# class Bellman_Ford(SPAlgorithm):
    
    
class A_Star(SPAlgorithm):
    def __init__(self):
        super().__init__()
    
    def calc_sp(self, G, s, d, h):
        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        Q = min_heap2.MinHeap([])
        nodes = list(G.adj.keys())

        #Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap2.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(s, 0)

        #Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key

            if current_node == d:
                break

            for neighbour in G.adj[current_node]:
                g_score = dist[current_node] + G.w(current_node, neighbour)
                if g_score < dist[neighbour]:
                    f_score = g_score + h(current_node, neighbour)  # total cost: g_score + heuristic
                    Q.decrease_key(neighbour, f_score)
                    dist[neighbour] = g_score
                    pred[neighbour] = current_node

        # Based off the numberphile video provided in the lab pdf, we start off from the destination node and build up to the source node
        path = []
        temp = d
        while temp in pred:
            path.insert(0, temp)
            temp = pred[temp]
        if path:
            path.insert(0, s)

        # Returning the tuple
        return path