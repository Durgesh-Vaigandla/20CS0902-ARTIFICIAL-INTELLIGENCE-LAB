def best_first_search(graph, start, goal, h): 
    visited = set() 
    pq = [(h[start], start)]  
    print("Best First Search Path:", end=" ") 
    while pq: 
        pq.sort()  
        cost, node = pq.pop(0)  
        if node in visited: 
            continue 
        print(node, end=" ") 
        if node == goal: 
            break 
        visited.add(node) 
        for neighbour in graph[node]: 
            if neighbour not in visited: 
                pq.append((h[neighbour], neighbour))  

graph = { 'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': [] } 
h = {'A': 5,'B': 3, 'C': 4,'D': 1,'E': 2,'F': 0} 
start = 'A' 
goal = 'F' 
print("Graph:", graph) 
print("Heuristic:", h) 
print("Start:", start) 
print("Goal:", goal) 
best_first_search(graph, start, goal, h)
