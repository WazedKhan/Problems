def minRemoveToMakeValid(s):
    stack = []
    string = list(s)

    for i in range(len(string)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                string[i] = ''
    for j in stack:
        string[j] = ''

    return ''.join(string)



s = "lee(t(c)o)de)"
# s = "a)b(c)d"
# s = "))(("
# s = "())()((("

print(minRemoveToMakeValid(s))