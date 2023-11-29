
import math
import csv
from pathlib import Path
import final_project_part1 as graph
from A_Star import a_star
import time
import matplotlib.pyplot as plt
import matplotlib as mpl

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
    G = graph.DirectedWeightedGraph()
    
    for station_id, _ in stations.items():
        G.add_node(station_id)
        
    for connection in conn:
        s1 = connection['station1']
        s2 = connection['station2']
        weight = connection['time']
        
        G.add_edge(s1,s2,weight)
        
    return G

def heuristic(station1, station2):
    stations = loadStations("london_stations.csv")
    lat1, lon1 = stations[station1]['latitude'], stations[station1]['longitude']
    lat2, lon2 = stations[station2]['latitude'], stations[station2]['longitude']
    
    return distance(lat1, lon1, lat2, lon2)
    
def run_experiment(G):
    a_star_times = []
    dijkstra_times = []
    
    for i, source in enumerate(G.adj.keys()):
        print(i)
        for j, destination in enumerate(G.adj.keys()):
            if source != destination:
                # Measure A* algorithm time
                start_time_astar = time.time()
                a_star(G, source, destination, heuristic)
                end_time_astar = time.time()
                a_star_times[i, j] = end_time_astar - start_time_astar

                # Measure Dijkstra's algorithm time
                start_time_dijkstra = time.time()
                graph.dijkstra(G, source, destination)
                end_time_dijkstra = time.time()
                dijkstra_times[i, j] = end_time_dijkstra - start_time_dijkstra

    # Plot results
    
    

s = loadStations("london_stations.csv")
c = loadConnections("london_connections.csv")
G = buildGraph(s,c)
print(run_experiment(G))



    
            
            