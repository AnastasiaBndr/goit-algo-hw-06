from collections import deque

def BFS_algorythm(graph,start):
	visited = set()
	queue = deque([start])

	while queue:
		vertex = queue.popleft()
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(set(graph.neighbors(vertex)) - visited)
	return visited 