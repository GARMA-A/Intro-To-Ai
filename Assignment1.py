import heapq
import random

# Define the Node class
class Node:
    def __init__(self, id, weight=0):
        self.id = id
        self.weight = weight

# Function to create a connected random graph
def generate_connected_graph(num_nodes):
    graph = {i: [] for i in range(num_nodes)}
    
    # Create a connected graph by ensuring every node has at least one edge
    for i in range(num_nodes - 1):
        weight = random.randint(1, 20)
        graph[i].append((i + 1, weight))
        graph[i + 1].append((i, weight))  # Ensure bidirectionality
    
    # Add additional random edges
    for i in range(num_nodes):
        num_extra_edges = random.randint(1, 3)  # Randomize additional edges
        for _ in range(num_extra_edges):
            target = random.randint(0, num_nodes - 1)
            if target != i and all(t[0] != target for t in graph[i]):
                weight = random.randint(1, 20)
                graph[i].append((target, weight))
                graph[target].append((i, weight))  # Bidirectional edge
    return graph

# A* algorithm using a combined weight
def a_star_algorithm(graph, start_id, target_id):
    open_set = []
    heapq.heappush(open_set, (0, start_id))  # (weight, node id)
    came_from = {}
    weights = {node: float('inf') for node in graph}
    weights[start_id] = 0

    while open_set:
        current_weight, current_id = heapq.heappop(open_set)

        # If we reached the target node
        if current_id == target_id:
            path = []
            while current_id in came_from:
                path.append(current_id)
                current_id = came_from[current_id]
            path.append(start_id)
            return path[::-1]

        for neighbor_id, edge_weight in graph[current_id]:
            tentative_weight = weights[current_id] + edge_weight
            if tentative_weight < weights[neighbor_id]:
                came_from[neighbor_id] = current_id
                weights[neighbor_id] = tentative_weight
                heapq.heappush(open_set, (tentative_weight, neighbor_id))
    return None

# Generate a graph with 20 nodes
random.seed(42)  # For reproducibility
test_graph = generate_connected_graph(20)

# Run the algorithm
start_node = 0
target_node = 19
shortest_path = a_star_algorithm(test_graph, start_node, target_node)

# Output the graph and shortest path
print("Generated Graph (Adjacency List):")
for node, edges in test_graph.items():
    print(f"{node}: {edges}")

print("\nShortest Path from Node", start_node, "to Node", target_node, ":")
print(shortest_path)