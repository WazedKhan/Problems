string = 'AABCAAADA'
k = 3
for i in range(0, len(string), k):
    q = ''
    for s in string[i:i+k]:
        if s not in q:
            q += s
    print(q)

