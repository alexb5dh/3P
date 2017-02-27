# Determines if there is a cycle in undirected graph with the help of union-find structure.

# TODO: estimate time and space complexities
# Time: 
# Space: 

from UnionFind import UnionFind
from collections import deque

# Graph represented as adjacency list dictionary: node -> [adjacent nodes].
# For implementation simplicitly graph is expected to be in 'tree-form',
# meaning that each edge occurs only once in all adjacency lists (from 'parent' to 'child').
# Otherwise main cycle should be changed to operate on graph edges directly.
def has_cycle(graph):
    if not len(graph): return False

    node_set = {node: UnionFind(node) for node in graph}

    for start in graph:
        for end in graph[start]:
            # key parameter in defaultdict factory callback would make it much simpler
            start_set = node_set.setdefault(start, UnionFind(start))
            end_set = node_set.setdefault(end, UnionFind(end))
            
            if not start_set.union(end_set): return True
            node_set[end] = node_set[start]
    
    return False

# Tests
from collections import defaultdict
from functools import partial
Graph = partial(defaultdict, list)

#   1
# 2   3
#    4 5
graph = Graph({
    1: [2, 3],
    3: [4, 5]
})
assert(not has_cycle(graph))

#   1
# 2   3
#   4
graph = Graph({
    1: [2, 3],
    2: [4],
    3: [4]
})
assert(has_cycle(graph))


#   1
# 2   3
#   4
graph = Graph({
    1: [2, 3],
    4: [2, 3]
})
assert(has_cycle(graph))

#   1
# 2   3
#   4
graph = Graph({
    1: [2, 3],
    2: [4],
    4: [3]
})
assert(has_cycle(graph))

# 1 2
# 3 4
graph = Graph({
    1: [2],
    3: [4],
})
assert(not has_cycle(graph))

# 1 2
# 3 4 3
graph = Graph({
    1: [2],
    3: [4],
    4: [3]
})
assert(has_cycle(graph))

from os import path
print (f'✔: {path.basename(__file__)}')
