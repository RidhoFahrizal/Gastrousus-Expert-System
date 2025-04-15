# Graph structure from the image
graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'D': 4, 'C': 6},
    'C': {'B': 6, 'E': 3},
    'D': {'F': 3, 'E': 5},
    'E': {'G': 2, 'D': 5},
    'F': {'Z': 2},
    'G': {'F': 6, 'Z': 3}
}

# Breadth First Search - manual implementation
def bfs(graph, start, goal):
    # Initialize queue with starting node
    queue = [(start, [start], 0)]  # (node, path, cost)
    visited = set()
    
    while queue:
        # Dequeue the first element (FIFO)
        node, path, cost = queue.pop(0)
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    queue.append((neighbor, new_path, new_cost))
    
    return None, float('inf')  # No path found

# Depth First Search - manual implementation
def dfs(graph, start, goal):
    # Initialize stack with starting node
    stack = [(start, [start], 0)]  # (node, path, cost)
    visited = set()
    
    while stack:
        # Pop the last element (LIFO)
        node, path, cost = stack.pop()
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            # Add neighbors to stack
            neighbors = list(graph.get(node, {}).items())
            for neighbor, weight in reversed(neighbors):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    stack.append((neighbor, new_path, new_cost))
    
    return None, float('inf')  # No path found

# Best First Search - manual implementation
def best_first_search(graph, start, goal):
    # Simple heuristic (estimated distance to goal)
    heuristic = {
        'A': 10, 'B': 8, 'C': 7, 
        'D': 6, 'E': 5, 'F': 2, 
        'G': 3, 'Z': 0
    }
    
    # Initialize open list with starting node
    open_list = [(heuristic[start], start, [start], 0)]  # (heuristic, node, path, cost)
    visited = set()
    
    while open_list:
        # Find node with minimum heuristic value
        min_index = 0
        for i in range(1, len(open_list)):
            if open_list[i][0] < open_list[min_index][0]:
                min_index = i
        
        # Remove and get the node with minimum heuristic
        _, node, path, cost = open_list.pop(min_index)
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    open_list.append((heuristic[neighbor], neighbor, new_path, new_cost))
    
    return None, float('inf')  # No path found

# Hill Climbing - manual implementation
def hill_climbing(graph, start, goal):
    # Simple heuristic (estimated distance to goal)
    heuristic = {
        'A': 10, 'B': 8, 'C': 7, 
        'D': 6, 'E': 5, 'F': 2, 
        'G': 3, 'Z': 0
    }
    
    current_node = start
    current_path = [start]
    total_cost = 0
    
    while current_node != goal:
        best_neighbor = None
        best_value = float('inf')
        
        # Find the neighbor with lowest heuristic value
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in current_path and heuristic[neighbor] < best_value:
                best_neighbor = neighbor
                best_value = heuristic[neighbor]
        
        # If no better neighbor found, we're stuck
        if best_neighbor is None:
            return None, float('inf')
        
        # Move to the best neighbor
        current_node = best_neighbor
        current_path.append(current_node)
        total_cost += graph[current_path[-2]][current_node]
        
        if current_node == goal:
            return current_path, total_cost
    
    return current_path, total_cost

# Branch and Bound - manual implementation
def branch_and_bound(graph, start, goal):
    # Initialize priority queue with starting node
    queue = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    
    while queue:
        # Find node with minimum cost
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
        
        # Remove and get the node with minimum cost
        cost, node, path = queue.pop(min_index)
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    queue.append((new_cost, neighbor, new_path))
    
    return None, float('inf')  # No path found

# Dynamic Programming - manual implementation
def dynamic_programming(graph, start, goal):
    # Gather all nodes
    nodes = set(graph.keys())
    for neighbors in graph.values():
        for node in neighbors:
            nodes.add(node)
    
    # Initialize distances and predecessors
    distances = {}
    predecessors = {}
    for node in nodes:
        distances[node] = float('inf')
        predecessors[node] = None
    
    # Set distance of start node to 0
    distances[start] = 0
    
    # Process all nodes
    for _ in range(len(nodes) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
    
    # Reconstruct path
    if distances[goal] == float('inf'):
        return None, float('inf')  # No path found
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = predecessors[current]
    
    # Reverse path to start from start node
    path.reverse()
    
    return path, distances[goal]

# Test each algorithm
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'Z'
    
    print("Breadth First Search:")
    bfs_path, bfs_cost = bfs(graph, start_node, goal_node)
    print(f"Path: {' -> '.join(bfs_path)}")
    print(f"Cost: {bfs_cost}")
    
    print("\nDepth First Search:")
    dfs_path, dfs_cost = dfs(graph, start_node, goal_node)
    print(f"Path: {' -> '.join(dfs_path)}")
    print(f"Cost: {dfs_cost}")
    
    print("\nBest First Search:")
    best_fs_path, best_fs_cost = best_first_search(graph, start_node, goal_node)
    print(f"Path: {' -> '.join(best_fs_path)}")
    print(f"Cost: {best_fs_cost}")
    
    print("\nHill Climbing:")
    hc_path, hc_cost = hill_climbing(graph, start_node, goal_node)
    print(f"Path: {' -> '.join(hc_path)}")
    print(f"Cost: {hc_cost}")
    
    print("\nBranch and Bound:")
    bb_path, bb_cost = branch_and_bound(graph, start_node, goal_node)
    print(f"Path: {' -> '.join(bb_path)}")
    print(f"Cost: {bb_cost}")
    
    print("\nDynamic Programming:")
    dp_path, dp_cost = dynamic_programming(graph, start_node, goal_node)
    print(f"Path: {' -> '.join(dp_path)}")
    print(f"Cost: {dp_cost}")