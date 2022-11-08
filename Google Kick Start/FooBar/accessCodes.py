from itertools import combinations

def checkTriples(luck):
    if int(luck[1]) % int(luck[0]) == 0 and int(luck[2]) % int(luck[1]) == 0:
        return True
    else: return False

def solution(l):
    num = ''
    for item in l:
        num += str(item)

    combi = combinations(num, 3)
    combi = [' '.join(i) for i in combi]

    count = 0

    for i in combi:
        val = "".join(i.split())
        if checkTriples(val) == True:
            count += 1
    return count


l = [1, 1, 1]

print(solution(l))