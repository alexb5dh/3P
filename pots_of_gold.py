# dynamic programming

# https://www.careercup.com/question?id=15422849

# Time: O(n^2)
# Space: O(n^2)

# Find winning strategy for first player in two-player game where they pick element from one of the arrays ends each turn.
# Player with maximum sum of elements wins. Assume that second player also tries to maximize his sum.
def pots_of_gold(pots): # todo: find better name
    memo = {}
    # moves = [None for p in pots]

    def dp(start, end): # todo: output sequence of turns
        if start > end: return 0
        if (start, end) in memo: return memo[(start, end)]

        a0b0, a0b1 = dp(start + 2, end), dp(start + 1, end - 1)
        a1b0, a1b1 = dp(start + 1, end - 1), dp(start, end - 2)

        a0 = pots[start] + min(a0b0, a0b1)
        a1 = pots[end] + min(a1b0, a1b1)
        memo[(start, end)] = max(a0, a1)

        # move_i = len(pots) - (end - start + 1)
        # if a0 >= a1:
        #     moves[move_i] = -1
        #     moves[move_i + 1] = -1 if a0b0 <= a0b1 else 1
        # else:
        #     moves[move_i] = 1
        #     moves[move_i + 1] = -1 if a1b0 <= a1b1 else 1
        
        return max(a0, a1)

    return dp(0, len(pots) - 1)
