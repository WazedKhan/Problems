def solution(initial, changes):
    for i in changes:
        initial += i

    if initial <= 1000:
        return "beginner"
    elif initial >= 1000 and initial < 1500:
        return "intermediate"
    elif initial >= 1500 and initial < 2000:
        return "advanced"
    elif initial >= 2000:
        return "pro"


print(solution(500, [1000, 2000]))
