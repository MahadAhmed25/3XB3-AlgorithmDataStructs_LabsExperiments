from collections import deque
from graph import Graph

#Breadth First Search That Returns the Path from Node1 to Node2
def BFS2(G, node1, node2):
    Q = deque([(node1, [node1])])
    marked = {node1 : True}
    
    while Q:
        current_node, path = Q.popleft()
        if current_node == node2:
            return path

        for neighbor in G.adj[current_node]:
            if not marked.get(neighbor, False):
                marked[neighbor] = True
                Q.append((neighbor, path + [neighbor]))

    return []


def main():
    g = Graph(6)
    g.add_edge(1,2)
    g.add_edge(2,5)
    g.add_edge(3,4)
    g.add_edge(4,5)
    
    print(BFS2(g, 1, 4))
    
main()