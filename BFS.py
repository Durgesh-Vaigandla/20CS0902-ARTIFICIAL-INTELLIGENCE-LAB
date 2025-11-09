graph = { 
    '5': ['3', '7'], 
    '3': ['2', '4'], 
    '7': ['8'], 
    '2': [], 
    '4': ['8'], 
    '8': [] 
}
def bfs(graph, start_node):
    visited = []  
    queue = []     

    queue.append(start_node)     
    visited.append(start_node)   
    while queue:
    m = queue.pop(0)         
    print(m, end=" ")        

    for neighbour in graph[m]:   
        if neighbour not in visited:
            visited.append(neighbour)   
            queue.append(neighbour)     
print("Following is the Breadth-First Search:") 
bfs(graph, '5')  
