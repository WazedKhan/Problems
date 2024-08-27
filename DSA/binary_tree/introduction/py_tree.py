class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


first_node = Node(2)
second_node = Node(3)
third_node = Node(4)
fourth_node = Node(5)


first_node.left = second_node
first_node.right = third_node
second_node.left = fourth_node



