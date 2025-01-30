

# **Greedy Algorithm**   vs **Dynamic Programming (DP)**       

| **Feature**           | **Greedy Algorithm**                         | **Dynamic Programming (DP)**             |
|-----------------------|---------------------------------------------|------------------------------------------|
| **Solution Process**   | Makes a locally optimal choice at each step | Solves subproblems and combines their solutions |
| **Key Properties Needed** | Greedy choice property and optimal substructure | Only optimal substructure required       |
| **Optimality**         | May not always yield a globally optimal solution | Always guarantees a globally optimal solution |
| **Efficiency**         | Faster and simpler, often \(O(n)\) or \(O(n \log n)\) | Slower and more complex, often \(O(n^2)\) or \(O(n \cdot W)\) |
| **Space Complexity**   | Typically lower                            | Typically higher due to memoization/table storage |
| **Problem Type**       | Works for problems with clear greedy choice property | Works for problems with overlapping subproblems |
| **Examples**           | - Dijkstra’s algorithm (shortest path with non-negative weights) <br> - Prim’s/Kruskal’s algorithms (Minimum Spanning Tree) <br> - Activity selection problem | - 0/1 Knapsack problem <br> - Longest Common Subsequence (LCS) <br> - Fibonacci sequence <br> - Bellman-Ford algorithm (shortest path with negative weights) |
| **Drawbacks**          | Doesn’t guarantee global optimum unless problem has greedy properties | Higher computational cost and memory usage |
| **When to Use**        | When greedy choice property applies, and local choices lead to global optimum | When the problem has overlapping subproblems and requires global optimization |





# 0/1 Knapsack Problem 

## Problem Statement

Given:
- A list of items, each with a specific value and weight.
- A knapsack with a maximum weight capacity.

Find the maximum value that can be achieved by selecting items without exceeding the knapsack's capacity, where each item can either be included in the knapsack or excluded.

## Algorithm

The solution uses **dynamic programming** to efficiently compute the maximum value:
- A 2D DP table (`dp[i][w]`) is used, where:
  - `i` represents the first `i` items considered.
  - `w` represents the weight capacity of the knapsack.
- The table is updated based on whether including the current item yields a higher value than excluding it.


### Code

```python
def knapsack(values, weights, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    :param values: List of item values
    :param weights: List of item weights
    :param capacity: Maximum capacity of the knapsack
    :return: Maximum value that can be obtained
    """
    n = len(values)
    # Create a 2D DP table to store the maximum value for each capacity and items
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:  # Can include the item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:  # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(values, weights, capacity)
print(f"The maximum value that can be obtained is: {max_value}")
```



# Longest Common Subsequence (LCS)

The **Longest Common Subsequence (LCS)** algorithm is a dynamic programming technique used to find the longest subsequence common to two sequences (strings, arrays, etc.) while maintaining the relative order of elements.

### Problem Definition
Given two sequences \( X = x_1, x_2, \ldots, x_m \) and \( Y = y_1, y_2, \ldots, y_n \), find the longest sequence \( Z \) that is a subsequence of both \( X \) and \( Y \).

### Properties of LCS
1. **Overlapping Subproblems**: The solution of the LCS can be broken down into smaller subproblems.
2. **Optimal Substructure**: The optimal solution of the problem depends on the optimal solutions of its subproblems.



### Algorithm: Dynamic Programming Approach

1. **Define the DP Table:**
   Let \( dp[i][j] \) represent the length of the LCS of the prefixes \( X[1:i] \) and \( Y[1:j] \).

2. **Base Cases:**
   - \( dp[0][j] = 0 \) for all \( j \): LCS of an empty string and any prefix of \( Y \) is 0.
   - \( dp[i][0] = 0 \) for all \( i \): LCS of any prefix of \( X \) and an empty string is 0.

3. **Recursive Relation:**
   For \( 1 \leq i \leq m \) and \( 1 \leq j \leq n \):
   - If \( X[i-1] == Y[j-1] \):  
     \[
     dp[i][j] = dp[i-1][j-1] + 1
     \]
   - Else:  
     \[
     dp[i][j] = \max(dp[i-1][j], dp[i][j-1])
     \]

4. **Result:**
   The length of the LCS is stored in \( dp[m][n] \).



### Code Implementation in Python
```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    i, j = m, n
    lcs_sequence = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_sequence.reverse()
    return dp[m][n], ''.join(lcs_sequence)

# Example Usage
X = "AGGTAB"
Y = "GXTXAYB"
length, sequence = lcs(X, Y)
print(f"LCS Length: {length}, LCS: {sequence}")
```



### Example
**Input:**
- \( X = \text{"AGGTAB"} \)
- \( Y = \text{"GXTXAYB"} \)

**Output:**
- LCS Length: \( 4 \)
- LCS: \( \text{"GTAB"} \)


### Time and Space Complexity
1. **Time Complexity:** 0(m.n) where  m and n are the lengths of x and y respectively.
2. **Space Complexity:** 
   - 0(m.n)  with the full DP table.
   - (O(min(m, n))) with space optimization (keeping only two rows of the DP table).
