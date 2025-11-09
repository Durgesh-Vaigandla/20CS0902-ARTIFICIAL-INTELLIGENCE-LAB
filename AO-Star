class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.best = None
    def add_child(self, relation, nodes, cost):
        self.children.append((relation, nodes, cost))

def aostar(node, graph, memo=None):
    if memo is None:
        memo = {}
    print(f"Visiting {node.name}")
    if not node.children:
        return 0, node.name
    if node.name in memo:
        return memo[node.name]
    best_cost = float("inf")
    best_choice = None
    for relation, children, cost in node.children:
        if relation == "OR":
            options = []
            for child in children:
                c_cost, c_sol = aostar(graph[child], graph, memo)
                options.append((cost + c_cost, (relation, [c_sol])))
            local_best = min(options, key=lambda x: x[0])
        else:
            child_results = [aostar(graph[ch], graph, memo) for ch in children]
            total_cost = cost + sum(c[0] for c in child_results)
            local_best = (total_cost, (relation, [c[1] for c in child_results]))
        if local_best[0] < best_cost:
            best_cost, best_choice = local_best
    node.best = best_choice
    memo[node.name] = (best_cost, (node.name, best_choice))
    print(f"Best option for {node.name} = {best_choice} with cost {best_cost}")
    return memo[node.name]

graph = {n: Node(n) for n in "ABCDE"}
graph['A'].add_child("OR", ['B'], 1)
graph['A'].add_child("OR", ['C'], 1)
graph['B'].add_child("AND", ['D', 'E'], 2)
graph['C'].add_child("OR", ['E'], 3)

cost, solution = aostar(graph['A'], graph)
print("\nOptimal Cost using AO*:", cost)
print("Solution Graph:", solution)
