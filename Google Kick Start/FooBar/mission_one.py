
def solution(s):
    duplicats = []
    res = []
    for i in range(1,len(s)+1):
        val = s[0:i]
        duplicats.append(val)

    for i in range(len(duplicats)):
        curr = duplicats[-i]

        if len(s.replace(curr,'')) == len(''):

            res.append(s.count(curr))

    return max(res)
s = "abcabcabcabc"

print(solution(s))
