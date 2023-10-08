from collections import deque
from graph import Graph

# Modified breadth first search that returns path from node 1 to node 2
def BFS2(G, node1, node2):
    Q = deque([(node1, [node1])])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node, path = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return path + [node2]
            if not marked[node]:
                Q.append((node, path + [node]))
                marked[node] = True
    return []

# Modified depth first search that returns path from node 1 to node 2
def DFS2(G, node1, node2):
    S = [(node1, [node1])]
    marked = {}
    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        current_node, path = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return path + [node2]
                S.append((node, path + [node]))
    return []


def main():
    g = Graph(6)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,5)
    g.add_edge(3,4)
    g.add_edge(4,5)
    
    print(BFS2(g, 1, 5))
    print(DFS2(g, 1, 5))
    
main()