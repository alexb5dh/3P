# arrays

# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

# Time: O(n)
# Space: O(1)

# Find minimum number of horizontal/vertical/diagonal steps in 2D plane
# to cover all points in enumerated order
def min_steps(points):
    return sum(max(
        abs(x[0] - y[0]),
        abs(x[1] - y[1])
    ) for x,y in pairwise(points))

from itertools import tee
def pairwise(iterable):
    g1, g2 = tee(iterable)
    next(g2)
    return zip(g1, g2)
