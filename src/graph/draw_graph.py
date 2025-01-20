import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G:nx.Graph):
    pos = nx.kamada_kawai_layout(G)
    plt.figure(figsize=(12, 12))
    central_stations = [node for node, degree in G.degree() if degree > 3]

    edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_size=120, node_color="skyblue", font_size=6, width=2,edge_color=edge_colors)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()