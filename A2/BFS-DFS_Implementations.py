from collections import deque
import random

from matplotlib import pyplot as plt
from graph import Graph
from graph import BFS

# Modified breadth first search that returns path from node 1 to node 2
def BFS2(g, node1, node2):
    # Storing both node and path (https://docs.python.org/3/library/collections.html#collections.deque)
    # need to use Q to keep track of the path since using array was adding neighbors for the inital node 
    Q = deque([(node1, [node1])])
    marked = {node1: True}
    for node in g.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node, path = Q.popleft()
        for node in g.adj[current_node]:
            if node == node2:
                return path + [node2]
            if not marked[node]:
                newPath = path + [node]
                Q.append((node, newPath))
                marked[node] = True
    return []

# Modified depth first search that returns path from node 1 to node 2
def DFS2(g, node1, node2):
    S = [(node1, [node1])]
    marked = {}
    for node in g.adj:
        marked[node] = False

    while len(S) != 0:
        current_node, path = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in g.adj[current_node]:
                if node == node2:
                    final_path = path + [node2]
                    return final_path
                newPath = path + [node]
                S.append((node, newPath))
    return []


# https://stackoverflow.com/questions/65622785/record-all-the-immediate-predecessors-in-the-bfs-algorithm
# Modified breadth first search that returns predecessor dicitonary
def BFS3(g, node1):
    Q = deque([node1])
    marked = {node1 : True}
    predDict = {}
    for node in g.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in g.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                predDict[node] = current_node
    return predDict

# https://stackoverflow.com/questions/66594717/depth-first-search-using-a-dictionary
# Modified depth first search that returns predecessor dicitonary
def DFS3(g, node1):
    S = [node1]
    marked = {}
    predDict = {}

    for node in g.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()

        if not marked[current_node]:
            marked[current_node] = True

            for node in g.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    if node not in predDict:
                        predDict[node] = current_node
    return predDict



# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
def has_cycle_util(G, node, visited, parent):
    visited[node] = True

    for i in G.adj[node]:
        if visited[i] == False:
            if has_cycle_util(G, i, visited, node):
                return True
        elif parent != i:
            return True
    return False

def has_cycle(G):
    visited = [False] * G.number_of_nodes()

    for i in range(G.number_of_nodes()):
        if visited[i] == False:
            if has_cycle_util(G, i, visited, -1):
                return True
    return False


def is_connected(G):
    start_node = list(G.adj.keys())[0]
    for target_node in G.adj:
        if not BFS(G, start_node, target_node):
            return False
    return True


def create_random_graph(i, j):
    g = Graph(i)
    edge_count = 0

    while edge_count < j:
        node1 = random.randint(0, i-1)
        node2 = random.randint(0, i-1)

        if node1 != node2 and not g.are_connected(node1, node2):
            g.add_edge(node1, node2)
            edge_count += 1
    return g


# Experiment 1
def experiment1(num_edges, num_nodes=100, num_trials=100):
    cycle_count = 0
    for _ in range(num_trials):
        G = create_random_graph(num_nodes, num_edges)
        if has_cycle(G):
            cycle_count += 1
            
    return cycle_count / num_trials

def graph_and_run_experiment1():
    edge_counts = []
    probabilities = []

    for num_edges in range(0, 200, 5):
        probability = experiment1(num_edges)
        edge_counts.append(num_edges)
        probabilities.append(probability)

    plt.plot(edge_counts, probabilities)
    plt.xlabel('Number of Edges')
    plt.ylabel('Probability of having a cycle')
    plt.title('Number of Edges vs Cycle Probability')
    plt.show()

# Experiment 2
def experiment2(num_edges, num_nodes=100, num_trials=100):
    connected_graphs = 0
    for _ in range(num_trials):
        G = create_random_graph(num_nodes, num_edges)
        if is_connected(G):
            connected_graphs += 1
            
    return connected_graphs / num_trials

def graph_and_run_experiment2():
    edge_counts = []
    probabilities = []

    for num_edges in range(0, 200, 5):
        probability = experiment2(num_edges)
        edge_counts.append(num_edges)
        probabilities.append(probability)

    plt.plot(edge_counts, probabilities)
    plt.xlabel('Number of Edges')
    plt.ylabel('Probability of being connected')
    plt.title('Number of Edges vs Probability of Connected Graph')
    plt.show()


def main():
    # bfs2 and dfs2 test
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,4)
    g.add_edge(2,3)
    g.add_edge(3,4)
    # print(BFS2(g, 0, 4))
    # print(DFS2(g, 0, 4))

    # bfs3 and dfs3 test
    g = Graph(6)
    g.add_edge(0,1)
    g.add_edge(1,3)
    g.add_edge(3,5)
    g.add_edge(0,2)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    print(BFS3(g, 0))
    print(DFS3(g, 0))


    # cycle is true test
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 2)  # edge creates cycle
    # print(has_cycle(g))

    # cycle is false test
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    # print(has_cycle(g))


    # is connected is true graph
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    # print(is_connected(g))

    # is connected is false graph
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    # print(is_connected(g))

    graph_and_run_experiment1()
    graph_and_run_experiment2()
    
main()