# binary tree, recursion

# https://www.interviewbit.com/problems/sorted-array-to-balanced-bst/

# Time: O(n)
# Space: O(log n)

# Construct balanced binary tree form sorted array
def btree_from_sorted_array(array, start = 0, end = None):
    if end is None: end = len(array)
    if end == start: return None

    mid = (start + end) // 2
    root = TreeNode(array[mid])
    root.left = btree_from_sorted_array(array, start, mid)
    root.right = btree_from_sorted_array(array, mid + 1, end)
    return root

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
