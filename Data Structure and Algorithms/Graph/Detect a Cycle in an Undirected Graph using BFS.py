from collections import deque

# Open input and output files
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

# Read the number of nodes (n) and edges (m)
n, m = [int(i) for i in f1.readline().split()]

# Construct adjacency list
adj_list = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = [int(i) for i in f1.readline().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs_cycle_detection(adj_list, start):
    color = {node: "white" for node in adj_list}
    parent = {node: None for node in adj_list}
    
    color[start] = "gray"
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if color[neighbour] == "white":
                color[neighbour] = "gray"
                parent[neighbour] = node
                queue.append(neighbour)
            elif parent[node] != neighbour:  # Found a back edge
                return True
        
        color[node] = "black"

    return False

# Check for cycles in all components
has_cycle = False
visited = set()
for node in range(1, n + 1):
    if node not in visited:
        if bfs_cycle_detection(adj_list, node):
            has_cycle = True
            break
        visited.update(adj_list.keys())  # Mark all reachable nodes as visited

# Write the result to the output file
f2.write("YES\n" if has_cycle else "NO\n")

f1.close()
f2.close()'
