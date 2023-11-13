class Graph:
    def __init__(self):
        self.vertices = {}
     # u = start vertex, v = end vertex
    def add_edge(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []

        self.vertices[u].append(v)
        self.vertices[v].append(u)

def dfs_traversal(graph, u, visited=None):
    if visited is None:
        visited = set()

    visited.add(u)
    print(u, end=" ")

    for neighbor in graph.get(u, []):
        if neighbor not in visited:
            dfs_traversal(graph, neighbor, visited)

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
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)

print("DFS traversal starting from vertex 1:")
dfs_traversal(g.vertices, 1)

print("\nBFS traversal starting from vertex 1:")
bfs_traversal(g.vertices, 1)
