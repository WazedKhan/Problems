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

# Breadth-First Search
# 1. Level order traversal


def breadth_first_search(root: Node):
    if root is None:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


breadth_first_search(root)
