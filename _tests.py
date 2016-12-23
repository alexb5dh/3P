from power import power
assert power(a = 0, n = 0) == 1
assert power(a = 0, n = 1) == 0
assert power(a = 0, n = 10) == 0
assert power(a = 1, n = 1) == 1
assert power(a = 1, n = 10) == 1
assert power(a = 2, n = 1) == 2
assert power(a = 2, n = 2) == 4
assert power(a = -2, n = 2) == 4
assert power(a = -2, n = 3) == -8
assert power(a = 2, n = 2 + 1) == 8
assert power(a = 2, n = 7) == 128
assert power(a = 2, n = 10) == 1024
print("✓: " + str(power))

from min_steps import min_steps
assert min_steps([(1,1), (1,1)]) == 0
assert min_steps([(1,1), (2,2)]) == 1
assert min_steps([(1,1), (2,3)]) == 2
assert min_steps([(1,1), (2,1)]) == 1
assert min_steps([(1,1), (2,2), (1,1)]) == 2
assert min_steps([(1,1), (2,3), (3,5)]) == 4
print("✓: " + str(min_steps))
