def countEleLessThanOrEqual():
    arr1 = [1,2,3,4,7,9]
    arr2 = [0,1,2,1,1,4]
    counter = []
    for i in range(len(arr1)):
        count = 0
        for j in arr2:
            if arr1[i] >= j:
                count+=1
        counter.append(count)
    return counter

print(countEleLessThanOrEqual())