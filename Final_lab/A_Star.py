import random
from final_project_part1 import create_random_complete_graph
import min_heap2

def a_star(G, s, d, h):
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

    # Returning the 2 tuple
    return pred, path


# # Testing
# nodes = 20
# upper = 20
# G = create_random_complete_graph(nodes, upper)
# s = random.randint(0, nodes - 1)
# d = random.randint(0, nodes - 1)

# def h(node1, node2):
#     return 1
    
# while d == s:  # making sure source and destination are not same
#     d = random.randint(0, nodes - 1)

# pred, path = a_star(G, s, d, h)

# print("Predecessor Dictionary:", pred)
# print("Shortest path from", s, "to", d, ":", path)