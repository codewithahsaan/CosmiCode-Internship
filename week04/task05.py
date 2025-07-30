import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to select the node with the smallest distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph (undirected)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 1},
    'E': {'D': 1}
}

# Get shortest paths from node A
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Display shortest paths
print(f"Shortest paths from node '{start_node}':")
for node, distance in shortest_paths.items():
    print(f" - To {node}: {distance}")
