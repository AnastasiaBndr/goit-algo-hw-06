import networkx as nx


def generate_graph(connections, stations, lines) -> nx.Graph:
    G = nx.Graph()
    for connection in connections:
        station1 = ""
        station2 = ""
        line_color = ""
        for station in stations:
            if station["id"] == connection["station1"]:
                station1 = station["name"]
            if station["id"] == connection["station2"]:
                station2 = station["name"]
        for line in lines:
            if connection["line"] == line["line"]:
                line_color = line["colour"]
        G.add_edge(station1, station2, color=line_color)
    return G
