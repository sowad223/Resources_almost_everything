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
