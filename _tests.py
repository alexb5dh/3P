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
assert max_subarray([1, -1, 1]) == (1, 0, 1)
assert max_subarray([-1, 1, -1]) == (1, 1, 2)
assert max_subarray([1, -3, 2, 1, -1]) == (3, 2, 4)
assert max_subarray([-1, -2, 3, 4, -5, 6]) == (8, 2, 6)
assert max_subarray([2, 3, -1, -20, 5, 10]) == (15, 4, 6)
assert max_subarray([1, 1, -1, -1, -1, 1, -1]) == (2, 0, 2)
assert max_subarray([1, -1, 1, -1, 1, 1, 1, -1]) == (3, 4, 7)
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == (6, 3, 7)
print("✓: " + str(max_subarray))

from min_max_division import min_max_division
# todo: tests for min_max_division

from number_solitaire import number_solitaire
# todo: tests for number_solitaire

from flip import flip
assert flip('111') == ()
assert flip('010') == (0,1)
assert flip('0011101') == (0,2)
assert flip('01010001') == (0, 7)
print("✓: " + str(flip))

from repeat_and_missing_numbers import repeat_and_missing_numbers
assert repeat_and_missing_numbers([3, 1, 2, 5, 3]) == (3, 4)
print("✓: " + str(repeat_and_missing_numbers))

from max_abs_diff_ind import max_abs_diff_ind
assert max_abs_diff_ind([1, 3, -1]) == 5
print("✓: " + str(max_abs_diff_ind))

from btree_from_sorted_array import btree_from_sorted_array
# todo: tests for btree_from_sorted_array

from max_depth import max_depth
# todo: tests for max_depth

from max_depth_nr import max_depth_nr
# todo: tests for max_depth_nr

from balanced_tree import balanced_tree
# todo: tests for balanced_tree

from gas_station import gas_station
assert gas_station(gas = [1, 2], cost = [2, 1]) == 1
assert gas_station(gas = [684, 57, 602, 987], cost = [909, 535, 190, 976]) == -1
print("✓: " + str(gas_station))
