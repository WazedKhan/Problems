def solution(l):
    sublist = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                sublist[i] = sublist[i] + 1
                count += sublist[j]

    return count


l = [1, 2, 3, 4, 5, 6,7,8,9,10]

print(solution(l))