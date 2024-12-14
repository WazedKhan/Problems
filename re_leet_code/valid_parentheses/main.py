def isValid(s):
    parentheses_hash = {")": "(", "}": "{", "]": "["}
    stack = []

    for i in s:
        if stack and i in parentheses_hash and stack[-1] == parentheses_hash[i]:
            stack.pop()
        else:
            stack.append(i)

    return not stack


s = "()[(]{)}"
print(isValid(s))
