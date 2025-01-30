











# Time Complexity



| **Algorithm**                     | **Best Case**          | **Average Case**       | **Worst Case**          | **Explanation**                                                                                                                                      |
|------------------------------------|------------------------|------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BFS (Breadth-First Search)**     | \( O(V+E) \)          | \( O(V+E) \)          | \( O(V+E) \)           | BFS visits each vertex and edge exactly once in an adjacency list. \( V \) is vertices, and \( E \) is edges.                                        |
| **DFS (Depth-First Search)**       | \( O(V+E) \)          | \( O(V+E) \)          | \( O(V+E) \)           | Similar to BFS, DFS visits each vertex and edge once but uses recursion or a stack.                                                                 |
| **Topological Sort**               | \( O(V+E) \)          | \( O(V+E) \)          | \( O(V+E) \)           | Performed using DFS. Requires \( O(V+E) \) to visit all nodes and edges in a Directed Acyclic Graph (DAG).                                           |
| **Strongly Connected Components**  | \( O(V+E) \)          | \( O(V+E) \)          | \( O(V+E) \)           | Performed using two DFS passes (e.g., Kosaraju's or Tarjan's algorithm). Each DFS is \( O(V+E) \).                                                  |
| **Dijkstra's Algorithm**           | \( O((V+E)log V)) | \( O((V+E)log V)) | \( O((V+E)log V))  | Using a priority queue, the time complexity is \( O((V+E) \log V) \). For dense graphs (\( E \approx V^2 \)), it becomes \( O(V^2 \log V) \).         |
| **Bellman-Ford Algorithm**         | \( O(VE) \)           | \( O(VE) \)           | \( O(VE) \)            | Iterates \( V-1 \) times over all \( E \) edges to relax distances. Works well for graphs with negative weights.                                     |
| **Kruskal's Algorithm**            | \( O(E \log E) \)     | \( O(E \log E) \)     | \( O(E \log E) \)      | Sorts edges by weight in \( O(E \log E) \) and uses a union-find data structure for detecting cycles, making it efficient for sparse graphs.          |
| **Prim's Algorithm**               | \( O((V+E) \log V) \) | \( O((V+E) \log V) \) | \( O((V+E) \log V) \)  | With a priority queue, it finds the MST in \( O((V+E) \log V) \). For dense graphs (\( E \approx V^2 \)), it becomes \( O(V^2 \log V) \).             |
---


# Preconditions and Use cases
| **Algorithm**                     | **Graph Type**                                    | **Preconditions**                                                                                                             | **Use Cases**                                                                                                               |
|------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **BFS (Breadth-First Search)**     | Any graph (directed/undirected, weighted/unweighted) | No special preconditions. Suitable for all graph types.                                                                      | - Finding shortest paths in **unweighted** graphs. <br> - Level-order traversal. <br> - Checking connectivity.              |
| **DFS (Depth-First Search)**       | Any graph (directed/undirected, weighted/unweighted) | No special preconditions. Suitable for all graph types.                                                                      | - Cycle detection. <br> - Pathfinding. <br> - Topological sort. <br> - Checking connectivity or reachability.              |
| **Topological Sort**               | Directed Acyclic Graph (DAG)                     | The graph **must be a DAG**. Cyclic graphs cannot have a valid topological ordering.                                         | - Scheduling tasks with dependencies (e.g., job scheduling). <br> - Dependency resolution in software packages.            |
| **Strongly Connected Components**  | Directed graph                                   | No special preconditions. Works on all directed graphs.                                                                      | - Identifying strongly connected components in directed graphs. <br> - Solving 2-SAT problems.                             |
| **Dijkstra's Algorithm**           | Weighted graph (directed or undirected)          | - Edge weights must be **non-negative**. <br> - Suitable for single-source shortest path calculation.                        | - Finding shortest paths in **non-negative weighted graphs**. <br> - GPS navigation. <br> - Network routing algorithms.     |
| **Bellman-Ford Algorithm**         | Weighted graph (directed or undirected)          | - Can handle **negative edge weights**, but not negative weight cycles. <br> - Suitable for single-source shortest path.     | - Shortest path calculation with negative weights. <br> - Detecting negative weight cycles.                                |
| **Kruskal's Algorithm**            | Weighted, connected, undirected graph            | - The graph must be **connected**. <br> - Works on undirected graphs only.                                                  | - Minimum Spanning Tree (MST) construction for cost optimization. <br> - Designing efficient network layouts.              |
| **Prim's Algorithm**               | Weighted, connected, undirected graph            | - The graph must be **connected**. <br> - Works on undirected graphs.                                                       | - Minimum Spanning Tree (MST) construction. <br> - Power grid or road network design.                                      |

---

### **Detailed Use Cases:**

1. **BFS**:
   - Best for finding the shortest path in **unweighted** graphs (e.g., solving maze problems).
   - Useful in level-based problems like finding the shortest path in a grid.

2. **DFS**:
   - Often used in problems involving connectivity, backtracking, or cycle detection.
   - Forms the foundation for algorithms like Topological Sort, SCCs, and others.

3. **Topological Sort**:
   - Crucial for task scheduling where dependencies exist, such as determining build orders in CI/CD pipelines.

4. **Strongly Connected Components**:
   - Helps break down directed graphs into strongly connected subgraphs.
   - Used in compiler optimization and circuit design.

5. **Dijkstra's Algorithm**:
   - Common in GPS and routing applications.
   - Used in finding the shortest path for network packets or navigation systems.

6. **Bellman-Ford Algorithm**:
   - Preferred for graphs with **negative edge weights**, e.g., economic or financial graphs with gain/loss cycles.
   - Detects negative weight cycles.

7. **Kruskal’s Algorithm**:
   - Used in MST construction for cost-saving designs in road or communication networks.
   - Performs well in sparse graphs due to sorting of edges.

8. **Prim’s Algorithm**:
   - Better suited for dense graphs compared to Kruskal’s.
   - Used for MST construction in infrastructure networks like electric grids or water supply systems.


## [Codes of Graphs](https://colab.research.google.com/drive/1-rhyRbdmgN280hvVJtBNwewwix28Eioo?usp=sharing)
# Graph Representation
## Adjacency Matrix
```python
# Read input and output file handles
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

# Read the number of nodes (n) and edges (m)
n, m = [int(x) for x in f1.readline().split()]

# Create an adjacency matrix initialized with zeros
adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]

# Fill adjacency matrix with edge weights
for _ in range(m):
    u, v, w = [int(x) for x in f1.readline().split()]
    adj_matrix[u][v] = w

# Write the adjacency matrix to the output file
for row in adj_matrix:
    f2.write(" ".join(map(str, row)) + "\n")

# Close input and output files
f1.close()
f2.close()
```

---

### Key Points:
1. **Adjacency Matrix Initialization**:  
   A 2D matrix of size `(n+1) x (n+1)` is created to include 1-based indexing.

2. **Edge Weight Assignment**:  
   Each edge is read, and the weight `w` is placed at position `[u][v]` in the matrix.

3. **Output Formatting**:  
   The adjacency matrix rows are converted to space-separated strings using `" ".join(map(str, row))`, ensuring clean output.


### Input (`input.txt`):
```
4 3
1 3 8
3 2 5
1 4 2
```

### Output (`output.txt`):
```
0 0 0 0 0
0 0 0 8 2
0 0 0 0 0
0 0 5 0 0
0 0 0 0 0
``` 


### Explanation of Output:
- The first row and column correspond to the 0-indexed dummy entries (for clarity with 1-based indexing).
- Edge `(1, 3)` has weight `8`, so `adj_matrix[1][3] = 8`.
- Edge `(3, 2)` has weight `5`, so `adj_matrix[3][2] = 5`.
- Edge `(1, 4)` has weight `2`, so `adj_matrix[1][4] = 2`.  
All other positions remain `0` since no edges exist for those pairs.


### **Adjacency List Representation of an Undirected Graph**

This code reads an undirected graph from an input file and generates its adjacency list representation. The graph's nodes (vertices) and edges are read as input, and the adjacency list is saved in an output file. 

---

### **Description**

- **Input**: 
  - The input file contains two integers `n` (number of nodes) and `m` (number of edges) on the first line. 
  - The following `m` lines contain two integers `u` and `v`, representing an undirected edge between node `u` and node `v`.

- **Output**: 
  - The adjacency list is written to an output file, where each line corresponds to a node. 
  - Each line starts with a node followed by a list of its neighbors (connected nodes).



### **Code**

```python
# Open input and output files
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

# Read the number of nodes (n) and edges (m)
n, m = [int(i) for i in f1.readline().split()]

# Initialize the adjacency list as a dictionary
adj_list = {}

# Read each edge and update the adjacency list
for i in range(m):
    u, v = [int(i) for i in f1.readline().split()]
    
    if u not in adj_list:
        adj_list[u] = []  # Initialize list if 'u' is not already in adj_list
    adj_list[u].append(v)
    
    if v not in adj_list:
        adj_list[v] = []  # Initialize list if 'v' is not already in adj_list
    adj_list[v].append(u)

# Write the adjacency list to the output file
for key in adj_list:
    f2.write(f"{key}: ")
    for val in adj_list[key]:
        f2.write(f"{val} ")
    f2.write("\n")

# Close the input and output files
f1.close()
f2.close()
```

---

### **Input File: `input.txt`**

```
9 8
1 2
1 3
1 4
2 5
4 6
4 7
6 8
3 9
```

---

### **Output File: `output.txt`**

```
1: 2 3 4 
2: 1 5 
3: 1 9 
4: 1 6 7 
5: 2 
6: 4 8 
7: 4 
8: 6 
9: 3 
```



### **Explanation**

1. **Input Breakdown**:
   - `n = 9` (number of nodes), `m = 8` (number of edges).
   - Edges: 
     - (1, 2), (1, 3), (1, 4), (2, 5), (4, 6), (4, 7), (6, 8), (3, 9)

2. **Adjacency List Representation**:
   - For each node, the code maintains a list of its neighbors (connected nodes).
   - For example:
     - Node `1` is connected to nodes `2`, `3`, and `4`.
     - Node `2` is connected to nodes `1` and `5`.

3. **Output**:
   - Each line starts with a node followed by the list of its connected nodes.


# Graph traversal

### Breadth-First Search (BFS)

The BFS algorithm explores a graph in layers, starting from a given node and systematically visiting all its neighbors before moving to the next layer. It ensures that each node is visited only once, using a queue for tracking nodes to explore and a visited list to avoid revisiting nodes.

1. **Adjacency List Representation**: The graph is represented as a dictionary, where keys are nodes, and values are lists of neighboring nodes.
2. **Visited Tracking**: A list ensures nodes are not revisited, maintaining the BFS traversal order.
3. **Queue**: The `Deque` (double-ended queue) ensures nodes are processed in the correct order.
4. **Traversal Order**: The result reflects the BFS traversal sequence, level by level.


### **Python Code Implementation**

```python
from collections import deque

def bfs(adj_list, start):
    visited = []  # To track visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    traversal = []  # To store BFS traversal order
    
    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            traversal.append(node)  # Add to traversal order
            for neighbor in adj_list[node]:  # Explore neighbors
                if neighbor not in visited:
                    queue.append(neighbor)  # Enqueue unvisited neighbors
    return traversal

```
### **Sample Input**

```
9 8
1 2
1 3
1 4
2 5
4 6
4 7
6 8
3 9
```


### **Output**

[1, 2, 3, 4, 5, 9, 6, 7, 8]





# Depth-First Search (DFS) Traversal

An algorithm to traverse a graph by exploring as far as possible along each branch before backtracking.

### Key Points
1. **Graph Representation**: Uses an adjacency list stored in a dictionary.
2. **Traversal Method**: Employs a stack to implement DFS iteratively.
3. **Visited Nodes**: Maintains a list of visited nodes to prevent revisiting.
4. **Start Node**: Begins traversal from a specified starting node (default: 1).
5. **Output**: Returns the order of nodes visited during traversal.

### Code
```python
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


```
# DFS Algorithm (Recursive)

```python
def dfs_recursive(adj_list, node, visited, traversal):
    visited.add(node)
    traversal.append(node)
    for neighbour in adj_list[node]:
        if neighbour not in visited:
            dfs_recursive(adj_list, neighbour, visited, traversal)

bfs_result = bfs(adj_list, start)
dfs_result = dfs(adj_list, start)

visited = set()
traversal = []
for node in adj_list:
    if node not in visited:
        dfs_recursive(adj_list, node, visited, traversal)



```

# An algorithm to explore a graph layer by layer, finding the shortest path in an unweighted graph.

```python
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


```







### Time Complexity
- **Construction of Adjacency List**: \(O(n + m)\), where \(n\) is the number of nodes and \(m\) is the number of edges.
- **DFS Traversal**: \(O(n + m)\), as each node and edge is processed once.
- **Overall Time Complexity**: \(O(n + m)\).

### Sample Input (input.txt)
```
6 6 5 
1 3 
3 2 
1 4 
2 6 
5 6 
4 6
```

### Output
```
[1, 4, 6, 5]
```

# Detect a Cycle in an Undirected Graph using BFS
Your code has a good structure but contains some issues. Let me explain and provide corrections:

1. **Input Assumption**: The code assumes that all nodes from 1 to `n` are present in the graph, but some nodes might not appear in the edges list. You need to ensure all nodes are included in the adjacency list.
  
2. **Output Handling**: The `print` statements will output results to the console, but the problem statement likely requires results in `output.txt`.

3. **Disconnected Graphs**: The BFS function assumes the graph is connected and starts from a single node. For disconnected graphs, cycle detection should handle all components.

4. **Starting Node**: The starting node is hard-coded as `1`, but this might not always be valid.

Here is the corrected and improved version:

```python
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
f2.close()
```


1. **Adjacency List Initialization**: Ensures all nodes from `1` to `n` are included in the adjacency list, even if they have no edges.
   
2. **Disconnected Components**: Handles graphs that are not connected by iterating over all nodes and checking each unvisited component.

3. **Visited Nodes Tracking**: Added a `visited` set to ensure no node is revisited.

4. **Output to File**: The result is written to `output.txt` as required.

5. **Generalized Starting Node**: Eliminates the hard-coded starting node, making it more robust for any input.



# **Cycle Detection in Directed Graph Using DFS with Integer Flags**

If you prefer using `0` and `1` instead of `False` and `True`, you can modify the algorithm accordingly. Here's the updated implementation using `0` for `False` and `1` for `True`:

### Python Implementation with `0` and `1`
```python
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
```

### Key Modifications
1. **Visited and Recursion Stack**:
   - `visited[node] == 0`: Node is unvisited.
   - `visited[node] == 1`: Node has been visited.
   - `rec_stack[node] == 0`: Node is not in the recursion stack.
   - `rec_stack[node] == 1`: Node is in the recursion stack.
   
2. **Return Values**:
   - `1`: Cycle detected.
   - `0`: No cycle detected.








# Topological Sort

**Topological Sort** is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge \( u \to v \), vertex \( u \) appears before \( v \) in the ordering. It is commonly used in scenarios like task scheduling, where some tasks must be completed before others.

### Properties
1. **Graph Type**: Only applicable to Directed Acyclic Graphs (DAGs).
2. **Ordering**: Provides a sequence that respects the dependencies (edges).

### Algorithms
#### 1. **Kahn’s Algorithm (Indegree-Based)**
   - Maintain an array of indegrees for each vertex.
   - Use a queue to store vertices with indegree 0.
   - Iteratively:
     - Remove a vertex from the queue and add it to the topological order.
     - Decrease the indegree of its neighbors. If a neighbor's indegree becomes 0, add it to the queue.

   **Time Complexity**: \( O(V + E) \), where \( V \) is the number of vertices and \( E \) is the number of edges.




### Kahn’s Algorithm (Indegree-Based)

```python
from collections import defaultdict, deque

def topological_sort_kahn(graph, vertices):
    indegree = {i: 0 for i in range(vertices)}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # Queue for nodes with indegree 0
    queue = deque([node for node in range(vertices) if indegree[node] == 0])
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == vertices:
        return topo_order  # Successfully sorted
    else:
        return "Cycle detected, topological sort not possible"

# Example usage
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
vertices = 4
print("Topological Sort (Kahn's Algorithm):", topological_sort_kahn(graph, vertices))
```
```
Topological Sort (Kahn's Algorithm): [0, 1, 2, 3]
```

#### 2. **Depth First Search (DFS) Based**
   - Perform DFS on the graph.
   - As you finish visiting all descendants of a node, push it onto a stack.
   - After the DFS completes, pop nodes from the stack to get the topological order.

   **Time Complexity**: \( O(V + E) \).


``` python
def topological_sort_dfs(graph, vertices):
    visited = [False] * vertices
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    for v in range(vertices):
        if not visited[v]:
            dfs(v)

    return stack[::-1]  # Reverse the stack for topological order


```
### Applications
- Task Scheduling.
- Course Prerequisite Ordering.
- Dependency Resolution in Build Systems (e.g., `make`).
- Compilation Order for Source Code Files. 


# Single-Source Shortest Path: Dijkstra's Algorithm

This repository contains an implementation of **Dijkstra's Algorithm** to compute the shortest paths from a source vertex to all other vertices in a weighted graph.

## Algorithm Overview

Dijkstra's Algorithm efficiently calculates the shortest paths from a single source vertex to all other vertices in a graph with **non-negative edge weights**.

### Key Features:
- Input: Weighted graph represented as an adjacency list.
- Output: A list of shortest path distances from the source vertex to all other vertices, with `-1` indicating unreachable vertices.
- Efficient handling of graph traversal using a **priority queue (min-heap)**.

## Implementation Details

### Input
- **`adj_list`**: An adjacency list where each vertex maps to a list of tuples `(neighbor, weight)` representing the edges and their weights.
- **`s`**: The source vertex.

### Output
- A list of shortest path distances from the source to each vertex:
  - `dist[v]`: The shortest distance from the source `s` to vertex `v`.
  - Unreachable vertices are marked as `-1`.


### Algorithm Steps

1. **Initialization**:
   - Set all distances to infinity (`math.inf`) except the source (`dist[s] = 0`).
   - Use a priority queue to store vertices with their distances, starting with the source.
   - Track visited vertices to prevent reprocessing.

2. **Process Each Vertex**:
   - Extract the vertex with the smallest distance.
   - For each neighbor, calculate the alternative distance (`alt = dist[u] + weight`).
   - Update the distance if `alt` is smaller than the current distance and push it into the queue.

3. **Output the Results**:
   - Convert all unreachable distances (`math.inf`) to `-1`.



### Complexity
- **Time Complexity**: \(O((V + E) \log V)\), where \(V\) is the number of vertices and \(E\) is the number of edges.
- **Space Complexity**: \(O(V + E)\).



## Example Usage

```python
import math
import heapq as hq

def dijkstra(adj_list, s):
    dist = [math.inf] * (len(adj_list) + 1)
    dist[s] = 0
    queue = []
    hq.heappush(queue, (dist[s], s))
    visited = [False] * (len(adj_list) + 1)

    while queue:
        curr_dist, u = hq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, weight in adj_list[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                hq.heappush(queue, (dist[v], v))

    return [-1 if d == math.inf else d for d in dist[1:]]

# Example Graph
adj_list = {
    1: [(2, 4), (3, 1)],
    2: [(3, 2), (4, 5)],
    3: [(4, 8)],
    4: []
}
source = 1

shortest_paths = dijkstra(adj_list, source)
print(shortest_paths)
```

## Notes
- Ensure that the graph contains **non-negative edge weights** for this algorithm to work correctly.
- For graphs with negative weights, consider the **Bellman-Ford algorithm**.



# **Kruskal's Minimum Spanning Tree Algorithm**


### Steps
1. **Initialize**:
   - Create a `parent` array where each element is its own parent.
   - Create a `size` array to keep track of the size of each component.
   - Set `min_spanning_tree_cost` to 0.

2. **Sort Edges**:
   - Sort the edges based on their weights.

3. **Union-Find**:
   - For each edge (u, v) with weight w:
     - Use the `find` function to get the roots of u and v.
     - If the roots are different, perform a union of the two components.
     - Add the weight of the edge to `min_spanning_tree_cost`.

4. **Return the Total Cost**:
   - After processing all edges, return the total cost of the minimum spanning tree.

### Key Information
- The algorithm works on undirected graphs.
- It employs a union-find data structure to efficiently manage and merge disjoint sets.
- The edge list is sorted, allowing the algorithm to consider the lowest-weight edges first.

### Code

```python
def find(parents, i):
    if parents[i] != i:
        parents[i] = find(parents, parents[i])
    return parents[i]

def union(parents, size, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)
    if root_x != root_y:
        # Ensure root_x is always the larger tree
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
        parents[root_y] = root_x
        size[root_x] += size[root_y]
    return size[root_x]

def kruskal(n, edges):
    parents = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    min_spanning_tree_cost = 0
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # Corrected the sort function

    for u, v, w in edges:
        if find(parents, u) != find(parents, v):
            min_spanning_tree_cost += w  # Add the weight to the cost
            union(parents, size, u, v)

    return min_spanning_tree_cost

# Sample input (number of vertices and edges)
n = 4  # Number of vertices
edges = [
    (1, 2, 10),
    (1, 3, 6),
    (1, 4, 5),
    (2, 4, 15),
    (3, 4, 4)
]

# Running the algorithm
result = kruskal(n, edges)
print("Minimum Spanning Tree Cost:", result)
```

### Input
```python
n = 4  # Number of vertices
edges = [
    (1, 2, 10),
    (1, 3, 6),
    (1, 4, 5),
    (2, 4, 15),
    (3, 4, 4)
]
```

### Output
```
Minimum Spanning Tree Cost: 15
```

![image](UnionFindKruskalDemo.gif)


### Explanation of the Output
- The edges chosen for the minimum spanning tree are:
  - (3, 4) with weight 4
  - (1, 4) with weight 5
  - (1, 2) with weight 10
- The total cost of the minimum spanning tree is 4 + 5 + 10 = 19.
