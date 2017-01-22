# 

# Elements of Programming Interviews in Java - 25.14

# Time: O(number_of_elements)
# Space: O(1) + O(number_of_elements)

# Assing positive number to elements such that element greater than his neighbour has greater value
# and sum of numbers are minimal
def fair_bonuses(elements): # todo: find better name
    vals = [1 for el in elements]

    for i in range(1, len(elements)):
        if elements[i] > elements[i-1]:
            vals[i] = vals[i-1] + 1

    for i in range(len(elements) - 2, 0, -1):
        if elements[i] > elements[i+1]:
            vals[i] = max(vals[i+1] + 1, vals[i])

    return vals
