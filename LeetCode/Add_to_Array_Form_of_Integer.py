def addToArrayForm(num, k):
    str_sum = ""
    for i in num:
        str_sum+=str(i)
    return [int(x) for x in str(int(str_sum)+k)]

num = [int(2), int(3)]
k = 181

print(addToArrayForm(num, k))