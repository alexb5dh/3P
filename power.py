# bit_manipulation

# Time: O(log n)
# Space: O(1)

# (int a, uint n) -> a^n
def power(a, n):
    res = 1
    while(n > 0):
        if n & 1: res *= a
        a = a * a
        n >>= 1
    return res
