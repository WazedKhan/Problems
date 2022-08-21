arr = [7, 69, 2, 221, 8974]
sum_ = []

for i in range(len(arr)):
    temp = arr[0]
    del arr[0]
    print(arr)
    sum_.append(sum(arr))
    arr.append(temp)

print(sum_)
print(min(sum_), max(sum_))
