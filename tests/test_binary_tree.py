from DSA.binary_tree.introduction.bfs_traversal import pre_order_dfs, Node


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


def test_pre_order_traversal_dfs():
    result = pre_order_dfs(root)
    assert result == [2, 3, 5, 4]
