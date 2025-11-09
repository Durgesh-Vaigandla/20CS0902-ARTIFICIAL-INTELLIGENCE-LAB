graph = { 
    '5': ['3', '7'], 
    '3': ['2', '4'], 
    '7': ['8'], 
    '2': [], 
    '4': ['8'], 
    '8': [] 
}
def bfs(graph, start_node):
    visited = []   # Keeps track of visited nodes
    queue = []     # Queue for BFS traversal

    queue.append(start_node)     # Start node is added to queue
    visited.append(start_node)   # Mark start node as visited
    while queue:
    m = queue.pop(0)         # Dequeue from front
    print(m, end=" ")        # Print current node

    for neighbour in graph[m]:   # Explore neighbors
        if neighbour not in visited:
            visited.append(neighbour)   # Mark visited
            queue.append(neighbour)     # Enqueue neighbor
print("Following is the Breadth-First Search:") 
bfs(graph, '5')  # Call bfs with graph and the starting node
