from src import generate_graph, draw_graph, open_file, DFS_algorythm, BFS_algorythm, dijkstra
import pandas as pd

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def pretty_print_dict(d):
    pretty_dict = ''  
     
    for k, v in d.items():
        pretty_dict += f'{k}: {v}\n'
    return pretty_dict
 
def main():

    path_stations = './src/data/lisbon.stations.csv'
    path_lines = './src/data/lisbon.lines.csv'
    path_connections = './src/data/lisbon.connections.csv'

    stations = open_file(path_stations)
    lines = open_file(path_lines)
    connections = open_file(path_connections)

    station="Bela Vista"

    G = generate_graph(connections, stations, lines)
    print(G)

    data = {
    f"{bcolors.OKGREEN}Depth-first search:{bcolors.ENDC}": DFS_algorythm(G,station),
    f"{bcolors.OKGREEN}Breadth-first search:{bcolors.ENDC}": list(BFS_algorythm(G, station))
}
    print(pd.DataFrame(data))
    print(f"{bcolors.OKGREEN}Dijkstra:\n{bcolors.ENDC} {pretty_print_dict(dijkstra(G, station))}")
    draw_graph(G)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
