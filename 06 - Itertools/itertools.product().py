

import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*tuple(itertools.product(A,B)))