import heapq
def astar(start, goal, graph, heuristic):
    open_list = [(heuristic[start], start)]
    came_from = {}
    g_cost = {start: 0}
    while open_list:
        h, current = heapq.heappop(open_list)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        for neighbor, cost in graph.get(current, {}).items():
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic.get(neighbor, float('inf'))
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current
    return None

graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 2, 'D': 5},
    'B': {'D': 1},
    'C': {'G': 5},
    'D': {'G': 2},
    'G': {}
}
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 5,
    'D': 1,
    'G': 0
}
start, goal = 'S', 'G'
path = astar(start, goal, graph, heuristic)
print("Graph:", graph)
print("Heuristic:", heuristic)
print("Start:", start)
print("Goal:", goal)
print("A* Search Path:", " -> ".join(path))
