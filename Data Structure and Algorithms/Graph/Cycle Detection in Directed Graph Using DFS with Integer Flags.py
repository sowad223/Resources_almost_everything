def is_cyclic(graph, num_nodes):
    visited = [0] * num_nodes  # 0 means unvisited, 1 means visited
    rec_stack = [0] * num_nodes  # 0 means not in recursion stack, 1 means in recursion stack

    def dfs(node):
        visited[node] = 1
        rec_stack[node] = 1

        for neighbor in graph[node]:
            if visited[neighbor] == 0:  # If neighbor is unvisited
                if dfs(neighbor):
                    return 1
            elif rec_stack[neighbor] == 1:  # If neighbor is in recursion stack
                return 1

        rec_stack[node] = 0  # Backtrack
        return 0

    for node in range(num_nodes):
        if visited[node] == 0:
            if dfs(node):
                return 1  # Cycle found

    return 0  # No cycle found

# Example usage:
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1],  # Cycle here
    4: []
}

print(is_cyclic(graph, 5))  # Output: 1 (Cycle exists)
