s = 'abbcccdddd'
queries = [1, 7, 5, 4, 15]
def weightedUniformStrings(s, queries):
    res = []
    last_str = ''
    weights = set()
    for i in range(len(s)):
        score = ord(s[i])-96
        ctr = ctr+1 if s[i] == last_str else 1
        last_str = s[i]
        weights.add((score*ctr))

    for i in queries:
        res.append('Yes') if i in weights else res.append('No')

    return res


print(weightedUniformStrings(s, queries))