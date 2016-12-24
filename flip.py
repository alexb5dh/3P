# Kadane's algorithm, Dynamic programming

# https://www.interviewbit.com/problems/flip/

# Time: O(n)
# Space: O(1)

# Find substring in the binary string 'flipping' which
# you get the most number of ones in the given string
# Leftmost and then shortest solution is preferred
def flip(string):
    nums = (-1 if c == '1' else 1 for c in string)

    first = next(nums)
    prev, best = (first, 0, 1), (first, 0, 1)
    for i, x in enumerate(nums, start = 1):
        if prev[0] < 0:
            curr = (x, i, i + 1)
        else:
            curr = (prev[0] + x, prev[1], i + 1)
        if curr[0] > best[0]:
            best = curr
        prev = curr
    return () if best[0] < 0 else (best[1], best[2])
