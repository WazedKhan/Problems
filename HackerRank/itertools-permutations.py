from itertools import permutations

s, n = input().split()

perms = sorted(list(permutations(s, int(n))))
for i in perms:
    print("".join(i))