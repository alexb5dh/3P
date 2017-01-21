# 

# https://www.careercup.com/question?id=5750868554022912

# Time: O(|cars|)
# Space: O(|cars|)

# Park cars in parking lot with one empty position in desired positions and return number of reparking actions
# This solution is not optimal
def car_parking_by_index(actual, desired):
    empty_i = next(i for i,c in enumerate(actual) if c is None)
    des_i_of = {c: i for i,c in enumerate(desired)}
    act_i_of = {c: i for i,c in enumerate(actual)}
    
    moves = 0
    for i,c in enumerate(actual):
        if c != desired[i]:
            moving_i, moving_c = act_i_of[desired[i]], desired[i]
            if c is not None:
                moves += 1
                actual[act_i_of[None]] = c
                act_i_of[c] = act_i_of[None]
                actual[i] = None
                act_i_of[None] = i

            if desired[i] is not None:
                moves += 1
                actual[moving_i] = None
                act_i_of[None] = moving_i
                actual[i] = moving_c
                act_i_of[moving_c] = i

    return moves
