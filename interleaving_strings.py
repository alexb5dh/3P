# dynamic programming

# https://www.interviewbit.com/problems/interleaving-strings/

# Time: O(len(s1) * len(s2))
# Space: O(len(s1) * len(s2))

# Determine if s3 can be obtained by interleaving s1 and s2
def interleaving_strings(s1, s2, s3):
    if(len(s3) != len(s1) + len(s2)): return False

    dp = [[None for __ in ' ' + s2] for _ in ' ' + s1]
    dp[0][0] = True
    for i in range(1, len(s1) + 1):
        dp[i][0] = s1[:i] == s3[:i]
    for j in range(1, len(s2) + 1):
        dp[0][j] = s2[:j] == s3[:j]
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = ((dp[i-1][j] and s1[i - 1] == s3[i + j - 1])
                     or (dp[i][j-1] and s2[j - 1] == s3[i + j - 1]))

    return dp[-1][-1]
