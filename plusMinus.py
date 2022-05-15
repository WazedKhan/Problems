arr = [1, 1, 0, -1, -1]

zero = 0
postive = 0
negative = 0

for i in arr:
    if i == 0:
        zero += 1
    if i > 0:
        postive += 1
    if i < 0:
        negative += 1

print("%6f" %(postive/len(arr)))
print("%6f" %(negative/len(arr)))
print("%6f" %(zero/len(arr)))