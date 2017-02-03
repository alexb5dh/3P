# dynamic programming

# 

# Time: O(n^2)
# Space: O(n)

# Find longest stronly increasing subsequence in sequence.
# Dynamic programming solution.
def longest_increasing_subsequence_dp(seq):
    dp = [1 for x in seq]

    for i in range(1, len(seq)):
        for j in range(0, i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
