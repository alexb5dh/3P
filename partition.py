# dynamic programming, no recursion

# 

# Time: O(total_weight * items)
# Space: O(total_weight)

# Determines if group of weights can be partitioned in two subgroups of equal total weight
def partition(weights):
    total = sum(weights)
    if total % 2 == 1: return False
    return _partition_(weights, total//2)

def _partition_(weights, weight_goal):
    prev_answers = [True] + ([False] * weight_goal)

    for weight in weights:
        new_answers = [None] * (weight_goal + 1)
        for w in range(weight):
            new_answers[w] = prev_answers[w]
        for w in range(weight, weight_goal + 1):
            new_answers[w] = (
                prev_answers[w] or
                prev_answers[w - weight]
            )
        prev_answers = new_answers
    
    return prev_answers[-1]
