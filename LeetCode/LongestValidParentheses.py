def longestValidParentheses(s):
    valid = [0]*len(s)
    stack = []

    for index, value in enumerate(s):
        if value == '(':
            stack.append(index)
        else:
            if stack:
                valid[stack.pop()] = 1
                valid[index] = 1

    longest = 0
    res = 0
    for i in valid:
        if i == 1: longest += 1
        else: longest = 0

        res = max(res, longest)

    return res




s = "()(()"
print(longestValidParentheses(s))