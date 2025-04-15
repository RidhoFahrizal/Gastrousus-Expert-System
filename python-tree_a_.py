# Graph structure dari Image 2
graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 7},
    'C': {'D': 2, 'Z': 2},
    'D': {'C': 2, 'Z': 5},
    'Z': {}
}

# 1. Breadth First Search
def bfs(graph, start, goal):
    # Inisialisasi queue dengan node awal
    queue = [(start, [start], 0)]  # (node, path, cost)
    visited = set()
    
    print("BFS Trace:")
    print(f"Queue: {queue}, Visited: {visited}")
    
    while queue:
        # Dequeue node pertama (FIFO)
        node, path, cost = queue.pop(0)
        
        print(f"Visiting: {node}, Path so far: {path}, Cost: {cost}")
        
        if node == goal:
            print(f"Goal reached: {node}")
            return path, cost
        
        if node not in visited:
            visited.add(node)
            print(f"Added to visited: {node}, Visited: {visited}")
            
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    queue.append((neighbor, new_path, new_cost))
                    print(f"Added to queue: {neighbor}, New path: {new_path}, New cost: {new_cost}")
                    print(f"Queue: {queue}")
    
    return None, float('inf')

# 2. Depth First Search
def dfs(graph, start, goal):
    # Inisialisasi stack dengan node awal
    stack = [(start, [start], 0)]  # (node, path, cost)
    visited = set()
    
    print("DFS Trace:")
    print(f"Stack: {stack}, Visited: {visited}")
    
    while stack:
        # Pop node terakhir (LIFO)
        node, path, cost = stack.pop()
        
        print(f"Visiting: {node}, Path so far: {path}, Cost: {cost}")
        
        if node == goal:
            print(f"Goal reached: {node}")
            return path, cost
        
        if node not in visited:
            visited.add(node)
            print(f"Added to visited: {node}, Visited: {visited}")
            
            # Tambahkan tetangga ke stack
            neighbors = list(graph.get(node, {}).items())
            for neighbor, weight in reversed(neighbors):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    stack.append((neighbor, new_path, new_cost))
                    print(f"Added to stack: {neighbor}, New path: {new_path}, New cost: {new_cost}")
                    print(f"Stack: {stack}")
    
    return None, float('inf')

# 3. Best First Search
def best_first_search(graph, start, goal):
    # Heuristik (perkiraan jarak ke tujuan)
    heuristic = {
        'S': 10,
        'A': 8,
        'B': 6,
        'C': 3,
        'D': 4,
        'Z': 0
    }
    
    # Inisialisasi open list dengan node awal
    open_list = [(heuristic[start], start, [start], 0)]  # (heuristic, node, path, cost)
    visited = set()
    
    print("Best First Search Trace:")
    print(f"Open list: {open_list}, Visited: {visited}")
    
    while open_list:
        # Temukan node dengan nilai heuristik terendah
        min_index = 0
        for i in range(1, len(open_list)):
            if open_list[i][0] < open_list[min_index][0]:
                min_index = i
        
        # Ambil node dengan heuristik minimum
        h_val, node, path, cost = open_list.pop(min_index)
        
        print(f"Visiting: {node}, Heuristic: {h_val}, Path so far: {path}, Cost: {cost}")
        
        if node == goal:
            print(f"Goal reached: {node}")
            return path, cost
        
        if node not in visited:
            visited.add(node)
            print(f"Added to visited: {node}, Visited: {visited}")
            
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    open_list.append((heuristic[neighbor], neighbor, new_path, new_cost))
                    print(f"Added to open list: {neighbor}, Heuristic: {heuristic[neighbor]}, New path: {new_path}, New cost: {new_cost}")
                    print(f"Open list: {open_list}")
    
    return None, float('inf')

# 4. Hill Climbing
def hill_climbing(graph, start, goal):
    # Heuristik (perkiraan jarak ke tujuan)
    heuristic = {
        'S': 10,
        'A': 8,
        'B': 6,
        'C': 3,
        'D': 4,
        'Z': 0
    }
    
    current_node = start
    current_path = [start]
    total_cost = 0
    
    print("Hill Climbing Trace:")
    print(f"Starting at: {current_node}, Heuristic: {heuristic[current_node]}")
    
    while current_node != goal:
        best_neighbor = None
        best_value = float('inf')
        
        # Temukan tetangga dengan nilai heuristik terendah
        print(f"Looking at neighbors of {current_node}:")
        for neighbor, weight in graph.get(current_node, {}).items():
            print(f"  Neighbor: {neighbor}, Heuristic: {heuristic[neighbor]}, Weight: {weight}")
            if neighbor not in current_path and heuristic[neighbor] < best_value:
                best_neighbor = neighbor
                best_value = heuristic[neighbor]
        
        # Jika tidak ada tetangga yang lebih baik, kita terjebak
        if best_neighbor is None:
            print("No better neighbor found. Stuck in local optima.")
            return None, float('inf')
        
        # Pindah ke tetangga terbaik
        print(f"Moving to best neighbor: {best_neighbor}, Heuristic: {best_value}")
        total_cost += graph[current_node][best_neighbor]
        current_node = best_neighbor
        current_path.append(current_node)
        print(f"Current path: {current_path}, Total cost: {total_cost}")
        
        if current_node == goal:
            print(f"Goal reached: {current_node}")
            return current_path, total_cost
    
    return current_path, total_cost

# 5. Branch and Bound
def branch_and_bound(graph, start, goal):
    # Inisialisasi priority queue dengan node awal
    queue = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    
    print("Branch and Bound Trace:")
    print(f"Queue: {queue}, Visited: {visited}")
    
    while queue:
        # Temukan node dengan biaya terendah
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
        
        # Ambil node dengan biaya minimum
        cost, node, path = queue.pop(min_index)
        
        print(f"Visiting: {node}, Path so far: {path}, Cost: {cost}")
        
        if node == goal:
            print(f"Goal reached: {node}")
            return path, cost
        
        if node not in visited:
            visited.add(node)
            print(f"Added to visited: {node}, Visited: {visited}")
            
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    queue.append((new_cost, neighbor, new_path))
                    print(f"Added to queue: {neighbor}, New path: {new_path}, New cost: {new_cost}")
                    print(f"Queue: {queue}")
    
    return None, float('inf')

# 6. Dynamic Programming
def dynamic_programming(graph, start, goal):
    # Kumpulkan semua node
    nodes = set(graph.keys())
    for neighbors in graph.values():
        for node in neighbors:
            nodes.add(node)
    
    # Inisialisasi jarak dan pendahulu
    distances = {}
    predecessors = {}
    for node in nodes:
        distances[node] = float('inf')
        predecessors[node] = None
    
    # Set jarak node awal ke 0
    distances[start] = 0
    
    print("Dynamic Programming Trace:")
    print(f"Initial distances: {distances}")
    print(f"Initial predecessors: {predecessors}")
    
    # Proses semua node
    for _ in range(len(nodes) - 1):
        print(f"\nIteration {_ + 1}:")
        for node in graph:
            for neighbor, weight in graph.get(node, {}).items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
                    print(f"Updated: {neighbor}, New distance: {distances[neighbor]}, Predecessor: {node}")
    
    print(f"\nFinal distances: {distances}")
    print(f"Final predecessors: {predecessors}")
    
    # Rekonstruksi jalur
    if distances[goal] == float('inf'):
        print("No path found to goal")
        return None, float('inf')  # Tidak ada jalur ditemukan
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = predecessors[current]
    
    # Balikkan jalur untuk dimulai dari node awal
    path.reverse()
    
    print(f"Reconstructed path: {path}, Total cost: {distances[goal]}")
    
    return path, distances[goal]

# Jalankan semua algoritma
if __name__ == "__main__":
    start_node = 'S'
    goal_node = 'Z'
    
    print("\n=== BREADTH FIRST SEARCH ===")
    bfs_path, bfs_cost = bfs(graph, start_node, goal_node)
    print(f"\nBFS Result - Path: {' -> '.join(bfs_path)}, Cost: {bfs_cost}")
    
    print("\n=== DEPTH FIRST SEARCH ===")
    dfs_path, dfs_cost = dfs(graph, start_node, goal_node)
    print(f"\nDFS Result - Path: {' -> '.join(dfs_path)}, Cost: {dfs_cost}")
    
    print("\n=== BEST FIRST SEARCH ===")
    best_fs_path, best_fs_cost = best_first_search(graph, start_node, goal_node)
    print(f"\nBest First Search Result - Path: {' -> '.join(best_fs_path)}, Cost: {best_fs_cost}")
    
    print("\n=== HILL CLIMBING ===")
    hc_path, hc_cost = hill_climbing(graph, start_node, goal_node)
    if hc_path:
        print(f"\nHill Climbing Result - Path: {' -> '.join(hc_path)}, Cost: {hc_cost}")
    else:
        print("\nHill Climbing failed to find a path")
    
    print("\n=== BRANCH AND BOUND ===")
    bb_path, bb_cost = branch_and_bound(graph, start_node, goal_node)
    print(f"\nBranch and Bound Result - Path: {' -> '.join(bb_path)}, Cost: {bb_cost}")
    
    print("\n=== DYNAMIC PROGRAMMING ===")
    dp_path, dp_cost = dynamic_programming(graph, start_node, goal_node)
    print(f"\nDynamic Programming Result - Path: {' -> '.join(dp_path)}, Cost: {dp_cost}")