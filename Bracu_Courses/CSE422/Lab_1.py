from queue import PriorityQueue

input_file = open("24141255_Showrin_CSE422_06_Lab_Assignment01_InputFile_Summer2024.txt", 'r')
graph = {}
for line in input_file:
    line_parts = line.split()
    node = line_parts[0]
    heuristic = int(line_parts[1])
    neighbour_nodes = {}
    for i in range(2, len(line_parts), 2):
        neighbour_node = line_parts[i]
        distance = int(line_parts[i + 1])
        neighbour_nodes[neighbour_node] = distance

    graph[node] = {"heuristic": heuristic, "neighbour": neighbour_nodes}


def A_star(graph, start, end):
    fringe = PriorityQueue()
    fringe.put((0, start))
    visited = {}
    start_to_current = {node: float('inf') for node in graph}
    start_to_current[start] = 0
    current_to_goal_heuristic = {node: float('inf') for node in graph}
    current_to_goal_heuristic[start] = graph[start]["heuristic"]

    while not fringe.empty():
        current_lowest_cost_node = fringe.get()[1]

        if current_lowest_cost_node == end:
            return visited_path(visited, current_lowest_cost_node,start_to_current)

        for neighbour_node, cost in graph[current_lowest_cost_node]["neighbour"].items():
            new_current_to_goal_heuristic = start_to_current[current_lowest_cost_node] + cost
            if new_current_to_goal_heuristic < start_to_current[neighbour_node]:
                visited[neighbour_node] = current_lowest_cost_node
                start_to_current[neighbour_node] = new_current_to_goal_heuristic
                total_cost = new_current_to_goal_heuristic + graph[neighbour_node]["heuristic"]
                fringe.put((total_cost, neighbour_node))
    return "NO PATH FOUND"

def visited_path(visited, current_lowest_cost_node,start_to_current):
    full_path = [current_lowest_cost_node]
    while current_lowest_cost_node in visited:
        current_lowest_cost_node = visited[current_lowest_cost_node]
        full_path.append(current_lowest_cost_node)
    full_path.reverse()
    total_distance = start_to_current[full_path[-1]]
    print(start_to_current)

    return full_path,total_distance

start = input("start node: ")
end = input("end node: ")
path,total_distance = A_star(graph, start, end)
print("Path:", path)
print("Total Distance: ",total_distance)
