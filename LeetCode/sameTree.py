# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p):
    stack = [p]
    res = []
    while stack:
        if stack:
            current = stack.pop()
            res.append(current.val)
        else:
            return False
        
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return res




a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

p = a

print(isSameTree(p))


