
import math
import csv
from pathlib import Path
import final_project_part1 as graph


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
        weight = distance(stations[s1]['latitude'], stations[s1]['longitude'], stations[s2]['latitude'], stations[s2]['longitude'])
        
        G.add_edge(s1,s2,weight)
        
    return G

s = loadStations("london_stations.csv")
c = loadConnections("london_connections.csv")
G = buildGraph(s,c)
    
            
            