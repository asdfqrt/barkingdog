import heapq
import math

# define a graph as a dictionary of dictionaries
graph = {
    (0, 0): {(1, 0): 1, (0, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1}
}

# define a heuristic function for A*
def heuristic(node, goal):
    # estimate the distance from node to goal
    return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

# define the A* algorithm
def a_star(graph, start, goal):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost
        for neighbor in graph[node].keys():
            heapq.heappush(heap, (cost + graph[node][neighbor] + heuristic(neighbor, goal), neighbor))
    return float('inf')

# define the Dijkstra's algorithm
def dijkstra(graph, start, goal):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost
        for neighbor in graph[node].keys():
            heapq.heappush(heap, (cost + graph[node][neighbor], neighbor))
    return float('inf')

# example usage
start = (0, 0)
goal = (1, 1)
print('A*: ', a_star(graph, start, goal))
print('Dijkstra: ', dijkstra(graph, start, goal))