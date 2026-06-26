class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


current = reverse_list(a)
print_linked_list(current)
