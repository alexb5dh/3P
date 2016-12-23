# binary search

# https://codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/

# Space: O(1)
# Time: O(log[sum(A)] * len(A))

# Divide array into k consecutive blocks while minimizing maximum sum
def min_max_division(k, m, a):
    l, r = max(a), sum(a)
    while(l < r):
        m = (l + r) / 2
        if(is_achievable(k, a, m)):
            r = m
        else:
            l = m + 1
    return r

def is_achievable(k, a, l):
    c,s = 0, 0
    for x in a:
        if x != 0 and k == 0: return False
        c, s = c + 1, s + x
        if s >= l:
            k = k - 1
            c, s = 1, (x if s > l else 0) 
            if s > 0 and k == 0: return False
    return True