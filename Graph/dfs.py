class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_traversal(self, start):
        visited = set()
        stack = [start]

        while stack:
            current = stack.pop()
            if current not in visited:
                print(current, end=" ")
                visited.add(current)
                stack.extend(neighbor for neighbor in self.graph.get(current, []) if neighbor not in visited)

# Example usage:
# Creating a graph: 1 - 2 - 3 - 4
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Performing DFS traversal starting from node 1
print("DFS traversal starting from node 1:")
g.dfs_traversal(1)
