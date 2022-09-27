n = int(input())

res = 0

for i in range(n):
    if sum(list(map(int, input().split(' ')))) >= 2:
        res += 1

print(res)