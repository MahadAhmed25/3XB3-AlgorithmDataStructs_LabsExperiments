import random
from graph import *

# Used flatten list form website: https://saturncloud.io/blog/how-to-flatten-a-list-of-lists-in-python/
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def nodes(G):
    key_listt = list(G.adj)
    return key_listt

def vertex_cover(adj_dic, set_c, G):
    adj2_dic = adj_dic
    set2_c = set_c

    for c in set2_c:
        adj2_dic.pop(c)

    nested_list = adj2_dic.values()
    flat_list = flatten_list(nested_list)
    
    for c in set2_c:        

        if (c in flat_list):
            while c in flat_list:
                flat_list.remove(c)
            
                
    if (flat_list== []):
        c_val=True
    else:
        c_val=False

    return c_val



def approx1(G):
    c = set()
    global c_val
    c_val = False

    while c_val ==False:
        v = 0 #assuming graph type's nodes are numbers, setting vertex to first node
        for i in range(G.number_of_nodes()):
            if (len(G.adjacent_nodes(i)) > len(G.adjacent_nodes(v))): 
                v = i
        
        c.add(v)
    
        G.adjacent_nodes(v).clear()
        for i in range(G.number_of_nodes()):
            if (v in G.adjacent_nodes(i)):
                G.adjacent_nodes(i).remove(v)
                
        
        adjval = [value for value in G.adj.values()]

        nested_list = adjval
        flat_list = flatten_list(nested_list)

        if (len(flat_list)==0):
            c_val = True
            break

        if(set(c).issubset(flat_list)):
            c_val= True
            #print("In")

        else:
            c_val= False
            #print("out")
            
    return(c)
    
    #print(G.adjacent_nodes(v)) #checks if exists in node's adjacent list
    #print(G.are_connected(1,5)) #checks if these two old vertex are still connected
    #print(G.adj) #prints entire dictionary(no sign of v's edges)

def approx2(G):
    c = set()
    global c_val
    c_val = False

    while c_val ==False:
        v = random.randint(0,(len(nodes(G))-1))
        while v in c:
            v = random.randint(0,(len(nodes(G))-1))
   
        c.add(v)

        c_val = vertex_cover(G.adj.copy(), c, G)  
    
    return c
    
def approx3(G):
    c = set()
    edge = []

    global c_val
    c_val = False

    while c_val ==False:

    
        u = random.randint(0,(len(nodes(G))-1))
        num_edges = len(G.adjacent_nodes(u))
        while (num_edges == 0):
            u = random.randint(0,(len(nodes(G))-1))
            num_edges = len(G.adjacent_nodes(u))
    
        v = G.adjacent_nodes(u)[0]

        edge.append(u)
        edge.append(v)
    
        c.add(u)
        c.add(v)
        #print(c)
        #print("EDGES", edge)

        G.adjacent_nodes(v).clear()
        for i in range(G.number_of_nodes()):
            if (v in G.adjacent_nodes(i)):
                G.adjacent_nodes(i).remove(v)
        
        G.adjacent_nodes(u).clear() #check question says to remive u OR v, I removed both v before this and u currently
        for i in range(G.number_of_nodes()):
            if (u in G.adjacent_nodes(i)):
                G.adjacent_nodes(i).remove(u)
        
        adjval = [value for value in G.adj.values()]
        nested_list = adjval
        flat_list = flatten_list(nested_list)

        if (len(flat_list)==0):
            c_val = True
            break

        if(set(c).issubset(flat_list)):
            c_val= True
            #print("In")

        else:
            c_val= False
            #print("out")


    return c



def main():
    print("-----Approx Alg 1 -----") 
    graph1 = Graph(6)
    graph1.add_edge(0,1)#
    graph1.add_edge(0,2)
    graph1.add_edge(1,4)#
    graph1.add_edge(2,3)
    graph1.add_edge(3,4)
    graph1.add_edge(1,5)#
    graph1.add_edge(1,3)#
    print(approx1(graph1))

    print("-----Approx Alg 2 -----") 
    graph2 = Graph(6)
    graph2.add_edge(0,1)#
    graph2.add_edge(0,2)
    graph2.add_edge(1,4)#
    graph2.add_edge(2,3)
    graph2.add_edge(3,4)
    graph2.add_edge(1,5)#
    graph2.add_edge(1,3)#
    print(approx2(graph2))

    print("-----Approx Alg 3 -----") 
    graph3 = Graph(6)
    graph3.add_edge(0,1)#
    graph3.add_edge(0,2)
    graph3.add_edge(1,4)#
    graph3.add_edge(2,3)
    graph3.add_edge(3,4)
    graph3.add_edge(1,5)#
    graph3.add_edge(1,3)#
    print(approx3(graph3))
              
    

main()