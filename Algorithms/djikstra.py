def dijkstra(graph, start):
    # Initialize distances and visited flags
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = {node: False for node in graph}

    # Dijkstra's algorithm
    for _ in range(len(graph)):
        # Find the unvisited node with the smallest tentative distance
        current_node = min((node for node in graph if not visited[node]), key=lambda node: distances[node])

        # Mark the current node as visited
        visited[current_node] = True

        # Update the distances of neighbors
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {result}")
