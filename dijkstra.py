# Dijkstra's algorithm
# Graph represented as weighted adjacency list dictionary: node -> [(weight, adjacent node)]

# Time: O(edges * log(vertices))
# Space: O(vertices)

from heapq import heappop, heappush

def dijkstra(graph, start):
    visited = set()
    distances = {**{node: float('inf') for node in graph}, **{start: 0}}
    # For simplicity assume nodes are some simple structures like numbers of short strings and can be compared easily
    # TODO: nodes themselves must never be compared
    edges = [(0, start, start)]

    while edges:
        # get next edge
        weight, prev, curr = heappop(edges)

        # update distance
        distances[curr] = min(distances[curr], distances[prev] + weight)

        # add adjacent nodes
        for weight, next_ in graph[curr]:
            if next_ in visited: continue
            heappush(edges, (weight, curr, next_))

        visited.add(curr)

    del distances[start]
    return distances

# Tests
from functools import partial
from collections import defaultdict
Graph = partial(defaultdict, list)

# Simple single connection
# A 1 B
graph = Graph({
    'A': [(1, 'B')],
    'B': [(1, 'A')]
})
assert dijkstra(graph, 'A') == {'B': 1}

# No connection
# A 
# B
graph = Graph({
    'A': [],
    'B': []
})
assert dijkstra(graph, 'A') == {'B': float('inf')}

# Simple triangle
#   B
#  2 2
# A 3 C
graph = Graph({
    'A': [(2, 'B'), (3, 'C')],
    'B': [(2, 'A'), (2, 'C')],
    'C': [(3, 'A'), (2, 'B')]
})
assert dijkstra(graph, 'A') == {'B': 2, 'C': 3}

# Non-Euclidean triangle with detour path shorter than direct one
#   B
#  2 2
# A 5 C
graph = Graph({
    'A': [(2, 'B'), (5, 'C')],
    'B': [(2, 'A'), (2, 'C')],
    'C': [(5, 'A'), (2, 'B')]
})
assert dijkstra(graph, 'A') == {'B': 2, 'C': 4}

# Final 'integration' test
#         B
#      2     3
# A 1 C 3 E 2 F
#   2 1     1
#     D 1 G 
graph = Graph({
    'A': [(1, 'C'), (2, 'D')],
    'B': [(2, 'C'), (3, 'F')],
    'C': [(1, 'A'), (2, 'B'), (3, 'E'), (1, 'D')],
    'D': [(2, 'A'), (1, 'C'), (1, 'G')],
    'E': [(3, 'C'), (2, 'F')],
    'F': [(3, 'B'), (2, 'E'), (1, 'G')],
    'G': [(1, 'D'), (1, 'F')]
})
assert dijkstra(graph, 'A') == {'B': 3, 'C': 1, 'D': 2, 'E': 4, 'F': 4, 'G': 3}

print(f'✔: {str(dijkstra)}')
