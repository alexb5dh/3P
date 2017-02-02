# dynamic programming

# Elements of Programming Interviews in Java - 17.2

# Time: O(s1 * s2)
# Space: O(s1 * s2)

# Computes Levenshtein distance between two strings.
def levenshtein_distance(s1, s2): # Todo: optimize space to min(s1,s2)
    i1, i2 = 0, 0
    memo = [[0 for x in ' ' + s2] for x in ' ' + s1]

    for i in range(1, len(s1) + 1):
        memo[i][0] = i
    for j in range(1, len(s2) + 1):
        memo[0][j] = j

    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                memo[i1][i2] = memo[i1-1][i2-1]
            else:
                memo[i1][i2] = 1 + min(memo[i1][i2-1],
                                       memo[i1-1][i2],
                                       memo[i1-1][i2-1])
    return memo[len(s1)][len(s2)]
