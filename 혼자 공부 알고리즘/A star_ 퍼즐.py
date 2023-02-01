import heapq

def sort_array(matrix):
    def f(matrix):
        return sum([abs(matrix[i][j] - (i * len(matrix) + j)) for i in range(len(matrix)) for j in range(len(matrix))])

    def astar(matrix):
        heap = [(f(matrix), 0, matrix)]
        visited = set()
        while heap:
            (cost, depth, node) = heapq.heappop(heap)
            node_int = 0
            for i in range(len(node)):
                for j in range(len(node)):
                    node_int = node_int * len(node) * len(node) + node[i][j]
            if node_int in visited:
                continue
            visited.add(node_int)
            if node == [[(i * len(matrix) + j) for j in range(len(matrix))] for i in range(len(matrix))]:
                return depth
            for i in range(len(node)):
                for j in range(len(node)):
                    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= ni < len(node) and 0 <= nj < len(node):
                            neighbor = [row[:] for row in node]
                            neighbor[i][j], neighbor[ni][nj] = neighbor[ni][nj], neighbor[i][j]
                            heapq.heappush(heap, (depth + 1 + f(neighbor), depth + 1, neighbor))

    return astar(matrix)

print(sort_array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])) # outputs 11