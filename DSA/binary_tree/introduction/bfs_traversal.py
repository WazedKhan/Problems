class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, head: Node) -> None:
        self.head = head

    # Pre-order DFS: Root, Left, Right
    def travel_pre_order(self):
        print("Pre-order DFS: Root, Left, Right: ", end=" ")
        if self.head is None:
            print("Provided Binary Tree is empty!")

        stack = [self.head]
        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # In-order DFS: Left, Root, Right
    def in_order_dfs(self):
        print("In-order DFS: Left, Root, Right: ", end=" ")
        if self.head is None:
            print("Provided Binary Tree is empty!")

        stack = []
        current = self.head

        while current or stack:
            # traverse left most element first
            while current:
                stack.append(current)
                current = current.left
            # check point where current none but stack is not
            current = stack.pop()
            print(current.value, end=" ")

            # as the all the left has visited now we go right and start from current light's left
            current = current.right


# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Building the tree
node1.left = node2  # 2 is the left child of 1
node1.right = node3  # 3 is the right child of 1
node2.left = node4  # 4 is the left child of 2
node2.right = node5  # 5 is the right child of 2

# Create BinaryTree with node1 as the head
binary_tree = BinaryTree(node1)
print(
    """ Tree:
                1
            2       3
        4       5
    """
)
# Testing pre-order traversal
binary_tree.travel_pre_order()
print()
binary_tree.in_order_dfs()
