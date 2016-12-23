from power import power
assert power(a = 0, n = 0) == 1
assert power(a = 0, n = 1) == 0
assert power(a = 0, n = 10) == 0
assert power(a = 1, n = 1) == 1
assert power(a = 1, n = 10) == 1
assert power(a = 2, n = 1) == 2
assert power(a = 2, n = 2) == 4
assert power(a = -2, n = 2) == 4
assert power(a = -2, n = 3) == -8
assert power(a = 2, n = 2 + 1) == 8
assert power(a = 2, n = 7) == 128
assert power(a = 2, n = 10) == 1024
print("✓: " + str(power))

from min_steps import min_steps
assert min_steps([(1,1), (1,1)]) == 0
assert min_steps([(1,1), (2,2)]) == 1
assert min_steps([(1,1), (2,3)]) == 2
assert min_steps([(1,1), (2,1)]) == 1
assert min_steps([(1,1), (2,2), (1,1)]) == 2
assert min_steps([(1,1), (2,3), (3,5)]) == 4
print("✓: " + str(min_steps))

from max_subarray import max_subarray
# todo: more tests for max_subarray
assert max_subarray([1, -3, 2, 1, -1]) == (3, 2, 4)
assert max_subarray([-1, -2, 3, 4, -5, 6]) == (8, 2, 6)
assert max_subarray([2, 3, -1, -20, 5, 10]) == (15, 4, 6)
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == (6, 3, 7)
print("✓: " + str(max_subarray))
