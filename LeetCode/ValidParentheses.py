s = "]"


def isValid(s: str):
    closing_bracket = ')}]'
    opening_bracket = '({['
    stack = []
    for i in s:
        if i in opening_bracket:
            stack.append(i)
        elif i in closing_bracket and stack:
            if stack[-1] == opening_bracket[closing_bracket.index(i)]:
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) < 1


print(isValid(s))