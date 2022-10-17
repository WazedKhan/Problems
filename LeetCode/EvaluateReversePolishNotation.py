import operator

def evalRPN(tokens):
    stack = []

    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }

    for i in tokens:
        if i not in ops:
            stack.append(int(i))
        else:
            operhand1 = stack.pop()
            operhand2 = stack.pop()
            res = ops[i](operhand2, operhand1)
            stack.append(int(res))
    return stack[0]

tokens = ["4","13","5","/","+"]

print(evalRPN(tokens))