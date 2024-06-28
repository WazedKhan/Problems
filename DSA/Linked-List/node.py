class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# A->B->C->D->null


def print_list(head: Node):
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result


# def print_list(head: Node):
#     if head is None:
#         return []
#     return [head.val] + print_list(head.next)


print(print_list(a))


# def sum_linked_list(head):
#     sum = 0
#     current = head
#     while current is not None:
#         sum += int(current.val)
#         current = current.next
#     return sum


def sum_linked_list(head):
    if head is None:
        return 0
    return head.val + sum_linked_list(head.next)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
print(sum_linked_list(a))
