# 

# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

# Find one number repeated twice and one missed
# in integer array from 1 to n
def repeat_and_missing_numbers(array):
    a_min_b = sum(x - i for (i, x) in enumerate(array, start = 1))
    a2_min_b2 = sum(x**2 - i**2 for (i, x) in enumerate(array, start = 1))

    a_plus_b = a2_min_b2 / a_min_b

    return ((a_plus_b + a_min_b) / 2, (a_plus_b - a_min_b) / 2)
