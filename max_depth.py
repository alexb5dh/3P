# binary tree, recursion

# https://www.interviewbit.com/problems/max-depth-of-binary-tree/

# Time: O(nodes)
# Space: O(max-depth)

# Find max depth of binary tree
def max_depth(root):
    return 1 + max(max_depth(root.left), max_depth(root.right)) if root else 0
