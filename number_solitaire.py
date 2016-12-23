# dynamic programming

# https://codility.com/programmers/lessons/17-dynamic_programming/number_solitaire/

# Space: O(1)
# Time: O(n)

#
def number_solitaire(a):
    n = len(a)
    dp = [a[0]] + [-float('inf')] * 7
    for start in xrange(0, n - 1):
        for dice in xrange(1, 7):
            if start + dice >= n: break
            dp[dice] = max(dp[dice + 1], dp[0] + a[start + dice])
        dp[0] = dp[1]
            
    return dp[0]
