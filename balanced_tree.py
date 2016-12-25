# binary tree, recursion

# https://www.interviewbit.com/problems/balanced-binary-tree/

# Time: O(nodes)
# Space: O(max-depth)

# Check if binary tree is balanced
def balanced_tree(root):
    if not root: return True
    if root.left and not root.right:
        return not root.left.left and not root.left.right
    if root.right and not root.left:
        return not root.right.left and not root.right.right
    return balanced_tree(root.left) and balanced_tree(root.right)
