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

    def append(self, new_data):
        # lets create a new node first
        new_node = Node(new_data)
        # case 1: if we have empty linked list, like our linked list is empty
        # in that case we can initialize the value in the first position
        if self.head is None:
            print(f"Head is empty: self.head = {self.head}")
            self.head = new_node
            return
        # case 2: our linked is not empty
        # in this case we need to find the last element of the linked list
        # as we want push at the end of the linked list
        last = self.head
        while last.next:
            # keep looking for last item of the linked list
            last = last.next
        # while loop make sure that we have our last element
        # now we can assign to next to our list element toward the new node
        last.next = new_node

    def print_nodes(self):
        result = []
        current_head = self.head
        while current_head is not None:
            result.append(current_head.data)
            current_head = current_head.next
        print(result)


linked_list = LinkedList()
linked_list.push("A")
linked_list.push("B")
linked_list.print_nodes()
linked_list.append("C")
linked_list.print_nodes()
