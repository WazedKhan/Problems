# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    stack = root
    values = []
    while root:
        current = stack.pop()
        values.append(current.val)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return values



root = [1,'null',2,3]
print(inorderTraversal(root))