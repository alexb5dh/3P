# Kadane's algorithm, Dynamic programming

# Time: O(n)
# Space: O(1)

# Find sum and indices for maximum sum subarray
# Leftmost solution is preferred even if it's longer
def max_subarray(array):
    prev, best = (0, -1, -1), (0, -1, -1)
    for i, x in enumerate(array):
        if x > prev[0] + x:
            curr = (x, i, i + 1)
        else:
            curr = (prev[0] + x, prev[1], i + 1)
        if curr[0] > best[0]:
            best = curr
        prev = curr

    return best
