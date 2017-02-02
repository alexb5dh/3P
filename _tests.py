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

from min_jumps import min_jumps
assert min_jumps([2,3,1,1,4]) == 2
print("✓: " + str(min_jumps))

from interleaving_strings import interleaving_strings
assert interleaving_strings('aabcc', 'dbbca', 'aadbbcbcac') == True
assert interleaving_strings('aabcc', 'dbbca', 'aadbbbaccc') == False
assert interleaving_strings('noU', '6i', 'n6ioU') == True
print("✓: " + str(interleaving_strings))

from car_parking_by_index import car_parking_by_index
actual, desired = [1, 2, 3, None, 4, 5], [1, 2, 3, None, 4, 5]
assert car_parking_by_index(actual, desired) == 0 and actual == desired
actual, desired = [1, 2, 3, None, 4, 5], [None, 2, 3, 1, 4, 5]
assert car_parking_by_index(actual, desired) == 1 and actual == desired
actual, desired = [1, 2, 3, None, 4, 5], [5, 1, None, 3, 2, 4]
assert car_parking_by_index(actual, desired) == 8 and actual == desired
actual, desired = [None, 1, 2, 3, 7, 6, 4, 5], [4, 6, 5, 1, 7, 3, 2, None]
assert car_parking_by_index(actual, desired) == 9 and actual == desired
print("✓: " + str(car_parking_by_index))

from smallest_range_all_arrays import smallest_range_all_arrays
assert smallest_range_all_arrays([1],
                                 [2],
                                 [3]) == (1,3)
assert smallest_range_all_arrays([4, 10, 15, 24, 26],
                                 [0, 9, 12, 20],
                                 [5, 18, 22, 30]) == (20, 24)
assert smallest_range_all_arrays([5, 10, 15],
                                 [3, 6, 9, 12, 15],
                                 [8, 16, 24]) == (15, 16)
print("✓: " + str(smallest_range_all_arrays))

from fair_bonuses import fair_bonuses
assert fair_bonuses([3, 4, 5, 2]) == [1,2,3,1]
assert fair_bonuses([1, 2, 4, 2, 1]) == [1, 2, 3, 2, 1]
print("✓: " + str(fair_bonuses))

from pots_of_gold import pots_of_gold
assert pots_of_gold([1, 2]) == 2
assert pots_of_gold([2, 5, 1, 1]) == 6
assert pots_of_gold([1, 2, 4, 8]) == 10
assert pots_of_gold([5, 5, 10, 5, 9, 9, 3, 9, 5, 1]) == 33
assert pots_of_gold([26, 1, 70, 11]) == 96
assert pots_of_gold([3, 9, 2, 1]) == 10
print("✓: " + str(pots_of_gold))

from levenshtein_distance import levenshtein_distance
assert levenshtein_distance('a', 'a') == 0
assert levenshtein_distance('a', 'b') == 1
assert levenshtein_distance('abc', 'acb') == 2
assert levenshtein_distance('hat', 'tape') == 3
assert levenshtein_distance('Carthorse', 'Orchestra') == 8
assert levenshtein_distance('abcdefg', 'xabxcdxxefxgx') == 6
print("✓: " + str(levenshtein_distance))
