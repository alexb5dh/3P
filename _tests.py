from power import *
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
