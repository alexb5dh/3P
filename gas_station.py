# 

# https://www.interviewbit.com/problems/gas-station/

# Time: O(n)
# Space: O(1)

# Find minimum index of gas station starting from which you can make a full cycle
def gas_station(gas, cost):
    start = 0
    while True:
        end, tank = travel(gas, cost, start)
        if tank >= 0 and end == start: return start
        if end < start: return -1
        if end == start and tank < 0: return -1
        start = end
    return start

def travel(gas, cost, start):
    curr, tank = start, 0
    while True:
        tank = tank + gas[curr] - cost[curr]
        curr = (curr + 1) % len(gas)
        if tank < 0 or curr == start:
            return curr, tank
