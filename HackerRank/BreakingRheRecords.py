def breakingRecords(scores):
    h_scores = []
    l_scores = []

    for i in range(len(scores)):
        if i != 0:
            h_scores.append(max(scores[:i]))
            l_scores.append(min(scores[:i]))

    h_scores = list(set(h_scores))
    l_scores = list(set(l_scores))

    for count, value in enumerate(h_scores):
        if value in l_scores:
            h_scores.remove(value)
            l_scores.remove(value)

    return [len(h_scores), len(l_scores)]

scores = list(map(int, '10 5 20 20 4 5 2 25 1'.rstrip().split()))
result = breakingRecords(scores)

print(result)