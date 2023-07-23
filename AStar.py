import heapq

def A_star(graph, start, goal):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == goal:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            heapq.heappush(heap, (cost + graph[current][neighbor], neighbor))

if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1},
    }
    start = 'A'
    goal = 'C'
    print("Cost from {} to {} is {}".format(start, goal, A_star(graph, start, goal)))
