# Floyd-Warshall algorithm for finding shortest path for all pairs of nodes in directed graph
# Graph represented as weighted adjacency list dictionary: node ->
# [(weight, adjacent node)]

# Time: O(vertices^3)
# Space: O(vertices^2)

from collections import defaultdict

def floyd_warshall(graph):
    # TODO: simplify distances matrix initialization
    distances = defaultdict(lambda: float('inf'))
    distances.update({(n, n): 0 for n in graph})
    distances.update({(n1, n2): w for n1 in graph for w, n2 in graph[n1]})

    for k in graph:
        for i in graph:
            for j in graph:
                distances[(i, j)] = min(
                    distances[(i, j)],
                    distances[(i, k)] + distances[(k, j)])

    # clear 0-length self-distances
    return {p: distances[p] for p in distances if p[0] != p[1]}

# Tests
from collections import defaultdict
from functools import partial
Graph = partial(defaultdict, list)

# TODO: add tests for Floyd-Warshall algorithm

# 'Integration' test
graph = Graph({
    '1': [(-2, '3')],
    '2': [(4, '1'), (3, '3')],
    '3': [(2, '4')],
    '4': [(-1, '2')]
})
assert (floyd_warshall(graph) == {
    ('1', '2'): -1,
    ('1', '3'): -2,
    ('1', '4'): 0,
    ('2', '1'): 4,
    ('2', '3'): 2,
    ('2', '4'): 4,
    ('3', '1'): 5,
    ('3', '2'): 1,
    ('3', '4'): 2,
    ('4', '1'): 3,
    ('4', '2'): -1,
    ('4', '3'): 1,
})

print(f'✔: str(floyd_warshall)')
