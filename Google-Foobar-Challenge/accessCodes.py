def solution(arr):
    sublist = [0] * len(arr)
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, i):
            if arr[i] % arr[j] == 0:
                sublist[i] = sublist[i] + 1
                count += sublist[j]

    return count


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(solution(arr))
