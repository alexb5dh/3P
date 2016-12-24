# 

# https://www.interviewbit.com/problems/maximum-absolute-difference/

# Time: O(n)
# Space: O(1)

# Find maximum value of |A[i] - A[j]| + |i - j|
# for array indices i,j of array A
def max_abs_diff_ind(array):
    inc = lambda: (x + i for (i,x) in enumerate(array))
    dec = lambda: (x - i for (i,x) in enumerate(array))
    return max((max(inc()) - min(inc()), max(dec()) - min(dec())))
