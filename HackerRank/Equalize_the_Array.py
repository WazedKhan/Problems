n = 5#int(input().strip())
arr = [1, 2, 3, 1, 2, 3, 3, 3]#list(map(int,)


import collections
equal_value = max(collections.Counter(arr).values())
print(len(arr) - max(collections.Counter(arr).values()))
