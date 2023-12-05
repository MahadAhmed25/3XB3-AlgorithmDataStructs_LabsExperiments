
import math
import csv
from pathlib import Path
import final_project_part1 as graph
from A_Star_Part2 import a_star
from GraphLibrary.ShortPathFinder import ShortPathFinder
from GraphLibrary.Graph import HeuristicGraph
from GraphLibrary.A_Star import A_Star
from GraphLibrary.Dijkstra import Dijsktra
import time
import matplotlib.pyplot as plt
import numpy

def loadStations(filename):
    filename = Path(__file__).with_name(filename)
    stations = {}
    
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station_id = int(row['id'])
            name = row['name']
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            stations[station_id] = {'name': name, 'latitude': latitude, 'longitude': longitude}
    return stations

def loadConnections(filename):
    filename = Path(__file__).with_name(filename)
    conn = []
    
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            s1 = int(row['station1'])
            s2 = int(row['station2'])
            line = int(row['line'])
            time = int(row['time'])
            conn.append({'station1': s1, 'station2': s2, 'line': line, 'time': time})
    return conn

#https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def distance(lat1, lon1, lat2, lon2):
    R = 6371
    Lat = math.radians(lat2-lat1)
    Lon = math.radians(lon2-lon1)
    a = math.sin(Lat/2) * math.sin(Lat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(Lon/2) * math.sin(Lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return (R * c) * 1000 #convert to meters

def buildGraph(stations, conn):
    G = HeuristicGraph()
    
    for station_id, _ in stations.items():
        G.add_node(station_id)
        
    for connection in conn:
        s1 = connection['station1']
        s2 = connection['station2']
        weight = connection['time']
        
        G.add_edge(s1,s2,weight)
        G.add_edge(s2,s1,weight)
        
    return G

def heuristic(s, sNode):
    h = {}
    slat, slon = s[sNode]['latitude'], s[sNode]['longitude']
    for station in s:
        stationLat, stationLon = s[station]['latitude'], s[station]['longitude']
        h[station] = distance(slat, slon, stationLat, stationLon)
        
    return h
        

#Experiment for all pairs of stations    
def run_experiment1(spf, stations = loadStations("london_stations.csv")):
    a_star_times = []
    dijkstra_times = []
    
    for i in spf.graph.adj.keys():
        s = i #chose start node
        h = heuristic(stations, s)
        spf.graph.set_heuristic(h)
        
        for j in spf.graph.adj.keys():
            d = j #chose end node
            
            if i == j: continue
                
            start = time.time()
            spf.set_algorithm(A_Star())
            spf.calc_short_path(s,d)
            a_star_times.append(time.time()-start)
            
            start = time.time()
            spf.set_algorithm(Dijsktra())
            spf.calc_short_path(s,d)
            dijkstra_times.append(time.time()-start)
    
    y = numpy.arange(len(a_star_times))
    
    plt.scatter(y, a_star_times, label = 'a_star')
    plt.scatter(y, dijkstra_times, label = 'dikstra')
    

    plt.xlabel('Trial#') 
    plt.ylabel('Time(s)') 
    
    plt.legend()
    plt.show() 
    
    #return average running times
    return sum(a_star_times)/len(a_star_times), sum(dijkstra_times)/len(dijkstra_times)

#Experiment for random start and end station
def run_experiment2(spf, stations = loadStations("london_stations.csv"), numTrials = 11):
    a_star_times = []
    dijkstra_times = []
    
    s = 1 #chose start node
    d = 300 #chose end node
    h = heuristic(stations, s)
    spf.graph.set_heuristic(h)
    
    for _ in range(numTrials):
        start = time.time()
        spf.set_algorithm(A_Star())
        spf.calc_short_path(s,d)
        a_star_times.append(time.time()-start)
        
        start = time.time()
        spf.set_algorithm(Dijsktra())
        spf.calc_short_path(s,d)
        dijkstra_times.append(time.time()-start)
    
    barWidth = 0.25
    
    br1 = numpy.arange(len(a_star_times))
    br2 = [x + barWidth for x in br1]
    
    plt.bar(br1, a_star_times, width=barWidth, edgecolor= 'grey', label = 'a_star')
    plt.bar(br2, dijkstra_times, width=barWidth, edgecolor= 'grey', label = 'dikstra')
    

    plt.xlabel('Trial#') 
    plt.ylabel('Time(s)') 
    
    plt.legend()
    plt.show() 
    
    #return average running times
    return sum(a_star_times)/len(a_star_times), sum(dijkstra_times)/len(dijkstra_times)

#Experiment for stations on the same line
def run_experiment3(spf, stations = loadStations("london_stations.csv"), connections = loadConnections("london_connections.csv")):
    a_star_times = []
    dijkstra_times = []
    
    s = 1 #chose start node
    line = connections[s]['line']
    h = heuristic(stations, s)
    spf.graph.set_heuristic(h)
    
    for i in spf.graph.adj.keys():
        d = i #chose end node
            
        if d == s: continue
        if connections[d]['line'] != line: continue
                
        start = time.time()
        spf.set_algorithm(A_Star())
        spf.calc_short_path(s,d)
        a_star_times.append(time.time()-start)
        
        start = time.time()
        spf.set_algorithm(Dijsktra())
        spf.calc_short_path(s,d)
        dijkstra_times.append(time.time()-start)
        
        
    
    barWidth = 0.25
    
    br1 = numpy.arange(len(a_star_times))
    br2 = [x + barWidth for x in br1]
    
    plt.bar(br1, a_star_times, width=barWidth, edgecolor= 'grey', label = 'a_star')
    plt.bar(br2, dijkstra_times, width=barWidth, edgecolor= 'grey', label = 'dikstra')
    

    plt.xlabel('Trial#') 
    plt.ylabel('Time(s)') 
    
    plt.legend()
    plt.show() 
    
    #return average running times
    return sum(a_star_times)/len(a_star_times), sum(dijkstra_times)/len(dijkstra_times)


def run_experiment4(spf, stations = loadStations("london_stations.csv")):
    a_star_times = []
    dijkstra_times = []
    y_distances = []
    
    s = 1 #chose start node
    h = heuristic(stations, s)
    spf.graph.set_heuristic(h)
    
    for i in spf.graph.adj.keys():
        d = i #chose end node
        if d == s: continue
        
        start = time.time()
        spf.set_algorithm(A_Star())
        dist = spf.calc_short_path(s,d)
        a_star_times.append(time.time()-start)
        y_distances.append(dist[1])
        
        start = time.time()
        spf.set_algorithm(Dijsktra())
        spf.calc_short_path(s,d)
        dijkstra_times.append(time.time()-start)
    
    
    plt.scatter(y_distances, a_star_times, label = 'a_star')
    plt.scatter(y_distances, dijkstra_times, label = 'dikstra')
    

    plt.xlabel('Node Distance') 
    plt.ylabel('Time(s)') 
    
    plt.legend()
    plt.show() 
    
    #return average running times
    return sum(a_star_times)/len(a_star_times), sum(dijkstra_times)/len(dijkstra_times)
    
    
        
    
    
    
if __name__ == "__main__":

    s = loadStations("london_stations.csv")
    c = loadConnections("london_connections.csv")
    
    spf = ShortPathFinder()
    
    G = buildGraph(s,c)
    spf.set_graph(G)
    
    #print(run_experiment1(spf, s)) # run experiment on all pairs of nodes
    #print(run_experiment2(spf, s, 11)) # chose start and end node and run experiment
    print(run_experiment3(spf, s, c)) # run experiment for start and end node on the same line
    #print(run_experiment4(spf, s)) # run experiment comparing node distance and running time
    

    
            
            