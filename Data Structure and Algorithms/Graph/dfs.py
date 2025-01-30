# Function to perform Depth-First Search (DFS) on the graph
def dfs(adj_list, start):
    visited = []  # List to track visited nodes
    stack = [start]  # Stack to manage DFS traversal
    traversal = []  # List to store the order of traversal

    while stack:
        node = stack.pop()  # Get the last node from the stack
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            traversal.append(node)  # Add the node to the traversal order
            for neighbor in reversed(adj_list[node]):  # Reverse neighbors for correct DFS order
                if neighbor not in visited:
                    stack.append(neighbor)  # Add unvisited neighbors to the stack

    return traversal

# Start DFS from node 1
start = 1
print(dfs(adj_list, start))  # Print the DFS traversal order


