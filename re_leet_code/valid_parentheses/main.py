from collections import Counter


def get_reverse_parentheses(char):

    if char == ")":
        return "("
    if char == "}":
        return "{"
    if char == "]":
        return "["


def isValid(s):
    parentheses_hash = {")": "(", "}": "{", "]": "["}

    stack = []
    count = 0
    for i in s:
        if stack and i in parentheses_hash and stack[-1] == parentheses_hash[i]:
            stack.pop()
        else:
            stack.append(i)

    return True if not stack else False


s = "()[(]{)}"
print(isValid(s))
