test = int(input())
for i in range(test):
    res = 0
    tem = input()
    list_ = list(map(int, input().split()))
    for i in list_:
        if i % 2 == 0:
            res += 1
    print(res)