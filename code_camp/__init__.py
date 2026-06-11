def get_expected_value(arr):
    optimistic = arr[1]
    realistic = arr[2]
    pessimistic = arr[3]
    idea_len = len(arr[0])
    expected = ((optimistic + 4 * realistic + pessimistic) / 6) * idea_len
    return expected


def analyze_ideas(ideas):
    sorted_ideas = sorted(ideas, key=get_expected_value)

    result = []

    for idea in sorted_ideas:
        result.append(idea[0])

    return result


res = analyze_ideas([["Add logging", 2, 5, 15], ["SEO optimization", 4, 8, 20], ["Fix bug", 1, 3, 5]])
print(res)
