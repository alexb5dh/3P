# binary tree

# https://www.interviewbit.com/problems/max-depth-of-binary-tree/

# Time: O(nodes)
# Space: O(max-depth)

# Find max depth of binary tree
# Uses two stacks instead of recursion
# http://stackoverflow.com/a/19914505/3542151
def max_depth_nr(root):
    depth = 0
    path, explore = [], [root]
    while explore:
        node = explore[-1]
        if path and path[-1] is node:
            depth = max(depth, len(path))
            explore.pop()
            path.pop()
        else:
            path.append(node)
            if node.left: explore.append(node.left)
            if node.right: explore.append(node.right)
    return depth
