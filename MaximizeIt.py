k, m = input().split()
max_values = 0
for _ in range(int(k)):
    max_value = max(list(map(int, input().split())))
    max_values += max_value * max_value

print(max_values % int(m))