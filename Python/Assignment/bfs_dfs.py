def dfs(adj_matrix, visited, node):
    visited[node] = True
    print(chr(node + 65), end=' ')  # Convert 0→A, 1→B, etc.
    for i in range(len(adj_matrix)):
        if adj_matrix[node][i] == 1 and not visited[i]:
            dfs(adj_matrix, visited, i)

# Adjacency Matrix
adj_matrix = [
    [0, 1, 1, 0],  # A
    [0, 0, 0, 1],  # B
    [0, 0, 0, 1],  # C
    [0, 0, 0, 0]   # D
]

print("DFS Traversal starting from A:")
visited = [False] * 4
dfs(adj_matrix, visited, 0)
##################################
from collections import deque

def bfs(adj_list, start):
    visited = [False] * len(adj_list)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(chr(node + 65), end=' ')  # Convert 0→A, 1→B, etc.
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# Adjacency List
adj_list = {
    0: [1, 2],  # A: B, C
    1: [3],     # B: D
    2: [3],     # C: D
    3: []       # D
}

print("\nBFS Traversal starting from A:")
bfs(adj_list, 0)
