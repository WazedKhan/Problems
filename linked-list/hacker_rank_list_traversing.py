# traversing a linked list and inserting at the end
# source: Hacker Rank Traversing: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true
# source: Hacker Rank Inserting: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?isFullScreen=true


class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append_node(self, val):
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
linked_list.append_node(1)
linked_list.append_node(2)
linked_list.append_node(3)
linked_list.display()  # Output: 1 -> 2 -> 3 -> None
