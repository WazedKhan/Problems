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
        5

    """
    print(tree)


# Pre-order DFS: Root, Left, Right
def pre_order_dfs(root: Node) -> None:
    print_tree()
    print("PRE ORDER DFS: ")
    if root is None:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data, end="")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print("\n")


# Post-order DFS: Left, Right, Root

# BFS: Level order traversal

pre_order_dfs(root)
