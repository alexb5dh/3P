# dynamic programming

# https://www.interviewbit.com/problems/min-jumps-array/

# Time: O(n^2)
# Space: O(n)

# Find minimum number of jumps required
# to reach last element in jumps array
def min_jumps(strength):
    jumps = [0] * len(strength)
    for i in range(len(strength) - 2, -1, -1):
        if strength[i] == 0:
            jumps[i] = float('inf')
        else:
            bound = min(len(jumps), i + strength[i] + 1)
            jumps[i] = 1 + min(jumps[j] for j in range(i + 1, bound))
            
    return jumps[0]
