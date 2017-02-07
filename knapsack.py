# dynamic programming, no recursion

# Elements of Programming Interviews in Java - 17.6

# Time: O(V * W)
# Space: O(W)

# Pack items in space-limited knapsack with maximum possible total value

# class Item:
#     def __self__(**kwargs args):
#         self.weight= args['weight']
#         self.value = args['value']

def knapsack(items, weight):
    v = 0
    prev_values = [0] * (weight + 1)
    
    for item in items:
        new_values = [0] * (weight + 1)
        for w in range(item.weight):
            new_values[w] = prev_values[w]
        for w in range(item.weight, weight + 1):
            new_values[w] = max(prev_values[w], prev_values[w - item.weight] + item.value)
        prev_values = new_values

    return prev_values[-1]
