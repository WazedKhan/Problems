# traversing a linked list and inserting at the end
# source: Hacker Rank Traversing: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true
# source: Hacker Rank Inserting at the end: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?isFullScreen=true
# source: Hacker Rank Inserting at the beginning: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?isFullScreen=true


class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, val):
        """
        inserts value at end of the linked list
        """
        # Create a new node for the given value
        new_node = Node(val)
        # Check if the list is empty (i.e., if the head is None)
        if self.head is None:
            # If the list is empty, set the new node as the head of the list
            self.head = new_node
        else:
            # If the list is not empty, start from the head
            current = self.head
            # Traverse the list until reaching the last node
            while current.next is not None:
                current = current.next
            # Once at the end of the list, set the next of the last node to the new node
            current.next = new_node

    def insert_at_beginning(self, val):
        """
        inserts value at the start of the linked list
        """
        # create a new node for given value
        new_node = Node(val)
        # set next node as the self head, basically we are merging self.head at the end of the new_node
        # in this way new node always will be the first node of the linked list
        new_node.next = self.head
        # now replace the self. head with new node as new node has the self.head merged at its end
        self.head = new_node

    def display(self):
        # Start from the head of the list
        current = self.head
        # Traverse the list and print each node's value
        while current:
            print(current.val, end=" -> ")
            current = current.next
        # Indicate the end of the list
        print("None")


# Example usage:
linked_list = LinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(3)
linked_list.display()
