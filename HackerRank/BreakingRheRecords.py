from typing import List


def breaking_records(scores: List[int]) -> List[int]:
    max_score = min_score = scores[0]
    max_count = min_count = 0
    for score in range(1, len(scores)):
        if scores[score] > max_score:
            max_score = scores[score]
            max_count += 1
        if scores[score] < min_score:
            min_score = scores[score]
            min_count += 1
    return [max_count, min_count]


scores = list(map(int, "10 5 20 20 4 5 2 25 1".rstrip().split()))
result = breaking_records(scores)

print(result)
