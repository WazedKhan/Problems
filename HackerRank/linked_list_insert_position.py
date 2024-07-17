# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Singly Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):

        # create a new node with new data
        new_node = Node(new_data)
        # as we are pushing at the beginning we point next node toward
        # like: new_node -> self.head(original node)
        new_node.next = self.head
        # now we can say new node as our original node
        self.head = new_node

    def insert(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertNodeAtPosition(self, data, position):
        # what I need to do:
        # I need to put given data on the given position
        # how can I do it?:
        # create new node for the given data
        # I can traverse through the link list and count its position
        # while traversing I need to keep track of previous item and current item kinda like slow pointer
        # if i find the given position then I can take its previous item and set next pointer to my new node
        # and new nodes pointer to the old current items next pointer
        # lets keep a flag to track previous item
        # Create a new node with the given data
        new_node = Node(data)

        # Initialize pointers and counter
        current = self.head
        previous = None
        counter = 0

        # Traverse the list to find the position to insert the new node
        while current is not None and counter < position:
            previous = current
            current = current.next
            counter += 1

        # Now insert the new node at the appropriate position
        if previous is None:
            # If position is 0, insert at the head
            new_node.next = self.head
            self.head = new_node
        else:
            # Insert between previous and current node
            previous.next = new_node
            new_node.next = current

    def print_nodes(self):
        result = []
        current_head = self.head
        while current_head is not None:
            result.append(current_head.data)
            current_head = current_head.next
        return result
