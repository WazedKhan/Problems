from os import name


class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None


# Creating the tree
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)


# root.left.right = Node(8)


def print_tree():
    print()
    tree = """
                2
            3       4
        5       6

    """
    print(tree)


# Pre-order DFS: Root, Left, Right
def pre_order_dfs(root: Node) -> None:
    stack = [root]
    current = root
    result = []
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


# Post-order DFS: Left, Right, Root

# BFS: Level order traversal

if name == __name__:
    print(pre_order_dfs(root))
