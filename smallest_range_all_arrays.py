# heap

# https://www.careercup.com/question?id=16759664
# Elements of Programming Interviews in Java - 15.6

# Time: O(total_size_of_arrays * ln(number_of_arrays))
# Space: O(number_of_arrays)

# Find smallest range containing at least one element from each array
from heapq import *

def smallest_range_all_arrays(*arrays):
    range = []
    for arr_i, arr in enumerate(arrays): # todo: switch to heapq.merge
        heappush(range, (arrays[arr_i][0], arr_i, 0))
    range_max = max(x[0] for x in range)
    
    min_range = (-float('inf'), float('inf'))
    while True:
        range_min, arr_i, i = range[0]
        if range_max - range_min < min_range[1] - min_range[0]: min_range = (range_min, range_max)

        arr, i = arrays[arr_i], i + 1
        if i >= len(arr): break
        range_max = max(range_max, arr[i])

        heapreplace(range, (arr[i], arr_i, i))

    return min_range
        