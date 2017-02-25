# graph, queue

# Time: O(nodes)
# Space: O(nodes)

from collections import deque

# Undirected graph breadth first traversal
# Graph represented as adjacency list dictionary: node -> [adjacent nodes]
def bfs(graph, root):
    queue = deque([root])
    visited = set()

    while queue:
        node = queue.popleft()

        if node in visited: continue
        visited.add(node)

        yield node
        for child in graph[node]:
            queue.append(child)

# Tests
from functools import partial
from collections import defaultdict
Graph = partial(defaultdict, list)

graph = Graph({
    1: [2, 3],
    2: [4]
})
assert(list(bfs(graph, 1))== [1, 2, 3, 4])

graph = Graph({
    1: [2, 3],
    2: [1, 4]
})
assert(list(bfs(graph, 1))== [1, 2, 3, 4])

print(f'✔: {str(bfs)}')
