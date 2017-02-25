# graph, dequeue

# Time: O(nodes)
# Space: O(nodes)

from collections import deque

# Undirected graph depth first traversal
# Graph represented as adjacency list dictionary: node -> [adjacent nodes]
def dfs(graph, root):
    queue = deque([root])
    visited = set()

    while queue:
        node = queue.popleft()
        
        if node in visited: continue
        visited.add(node)
        yield node

        for child in reversed(graph[node]):
            queue.appendleft(child)

# Tests
from functools import partial
from collections import defaultdict
Graph = partial(defaultdict, list)

graph = Graph({
    1: [2, 3],
    2: [4]
})
assert(list(dfs(graph, 1))== [1, 2, 4, 3])

graph = Graph({
    1: [2, 3],
    2: [1, 4]
})
assert(list(dfs(graph, 1))== [1, 2, 4, 3])

print(f'✔: {str(dfs)}')

