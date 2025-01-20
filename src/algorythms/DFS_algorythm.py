def DFS_algorythm(graph, vertex, visited=None):
    arr = []
    recursive(arr, graph, vertex, visited)
    return arr


def recursive(arr, graph, vertex, visited):
    if visited is None:
        visited = set()
    visited.add(vertex)
    arr.append(vertex)
    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            recursive(arr, graph, neighbor, visited)
