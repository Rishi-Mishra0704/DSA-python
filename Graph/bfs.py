class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = []
        self.vertices[u].append(v)

def bfs_traversal(graph, u):
    visited = set()
    queue = [u]

    while queue:
        current_vertex = queue.pop(0)
        if current_vertex not in visited:
            print(current_vertex, end=" ")
            visited.add(current_vertex)
            queue.extend(neighbor for neighbor in graph.get(current_vertex, []) if neighbor not in visited)

# Example usage:
print("BFS traversal:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
bfs_traversal(g.vertices, 1)
