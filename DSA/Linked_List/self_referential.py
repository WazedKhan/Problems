"""
Implementation of LinkedList Data structure in Python
"""


# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class


class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    # function insert a new node at the beginning
    def push(self, data):
        # 1 & 2: allocate the Node and put in the data
        new_node = Node(data=data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node


# Create a new linked list
my_linked_list = LinkedList()

# Test the push method to insert nodes at the beginning
my_linked_list.push(1)
my_linked_list.push(2)
my_linked_list.push(3)

# Print the linked list to verify the insertions
# It should print: 3 -> 2 -> 1

current_node = my_linked_list.head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")

# You can also add more test cases to test other methods you might implement
