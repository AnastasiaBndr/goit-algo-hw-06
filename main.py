from src import generate_graph, draw_graph, open_file
import networkx as nx
import matplotlib.pyplot as plt

def main():

    path_stations='./src/data/lisbon.stations.csv'
    path_lines='./src/data/lisbon.lines.csv'
    path_connections='./src/data/lisbon.connections.csv'


    stations=open_file(path_stations)
    lines=open_file(path_lines)
    connections=open_file(path_connections)

    graph= generate_graph(connections, stations,lines)

    draw_graph(graph)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)