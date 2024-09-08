from typing import List


def solvable_problem(n: int, surety: List[list]) -> int:
    result = 0
    for i in range(n):
        if sum(surety[i]) >= 2:
            result += 1
    return result


surety = []
n = 3
for i in ["1 1 0", "1 1 1", "1 0 0"]:
    temp_list = list(map(int, i.split(" ")))
    surety.append(temp_list)

print(solvable_problem(n, surety))
