# Kadane's algorithm, Dynamic programming

# Time: O(n)
# Space: O(1)

# Find sum and indices for maximum sum subarray
# Shortest and then leftmost solution is preferred
# Empty array is allowed
def max_subarray(array):
    prev, best = (0, -1, -1), (0, -1, -1)
    for i, x in enumerate(array):
        if prev[0] <= 0:
            curr = (x, i, i + 1)
        else:
            curr = (prev[0] + x, prev[1], i + 1)
        if curr[0] > best[0]:
            best = curr
        prev = curr

    return best
