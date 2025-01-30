def bfs_shortest_path_distance(adj_list, start, end):
    color = {node: "white" for node in adj_list}
    distance = {node: float('inf') for node in adj_list}
    parent = {node: None for node in adj_list}
    traversal_order = []
    
    color[start] = "gray"
    distance[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
            
        for neighbour in adj_list[node]:
            if color[neighbour] == "white":
                color[neighbour] = "gray"
                distance[neighbour] = distance[node] + 1
                parent[neighbour] = node
                queue.append(neighbour)
        
        color[node] = "black"

    return distance, parent, traversal_order

def reconstruct_path(parent, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    path.reverse() 
    return path

start = 1
distances, parents, traversal_order = bfs_shortest_path_distance(adj_list, start, e)
shortest_path = reconstruct_path(parents, start, e)
print("Distances:", distances)
print("Parents:", parents)
print("Traversal order:", traversal_order)
print("Shortest path from {} to {}: {}".format(start, e, shortest_path))

