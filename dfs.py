# graph, dequeue, no recursion

# 

# Time: O(nodes)
# Space: O(nodes)

from collections import deque

# Graph depth first traversal
def dfs(root):
    queue = deque([root])
    visited = set()

    while queue:
        node = queue.popleft()
        
        if node.value in visited: continue
        visited.add(node.value)
        yield node

        for child in reversed(node.children):
            queue.appendleft(child)
