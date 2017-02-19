# graph, queue, no recursion

# 

# Time: O(nodes)
# Space: O(nodes)

from collections import deque

# Graph breadth first traversal
def bfs(root):
    queue = deque([root])
    visited = set()

    while queue:
        node = queue.popleft()
        
        if node.value in visited: continue
        visited.add(node.value)
        yield node

        for child in node.children:
            queue.append(child)
