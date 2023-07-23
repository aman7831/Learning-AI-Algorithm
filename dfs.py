# adjacency list representation of a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set() # set to store visited vertices

def dfs(vertex):
    visited.add(vertex)
    print(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor)

# driver code
dfs('A') # prints A B D E C F
