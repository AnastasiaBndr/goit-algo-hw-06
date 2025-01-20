from src import generate_graph, draw_graph, open_file, DFS_algorythm,BFS_algorythm, dijkstra
import matplotlib.pyplot as plt
import networkx as nx

def main():

    path_stations='./src/data/lisbon.stations.csv'
    path_lines='./src/data/lisbon.lines.csv'
    path_connections='./src/data/lisbon.connections.csv'

    stations=open_file(path_stations)
    lines=open_file(path_lines)
    connections=open_file(path_connections)

    G= generate_graph(connections, stations,lines)
    # print(G.adjacency().toArray())

    # A = nx.adjacency_matrix(G)
    # print(A)

    # draw_graph(G)
    # print(DFS_algorythm(G,"Saldanha"))
    print(BFS_algorythm(G, "Saldanha"))
    # dijkstra(graph)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)