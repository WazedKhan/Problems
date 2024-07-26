class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to add a new node in the beginning of the linked list


def pushNode(head_ref, data_val):
    new_node = Node(data_val)
    new_node.next = head_ref[0]
    head_ref[0] = new_node

# Function to get the middle value of the linked list


def get_middle_brute_force(head):
    """Find middle of the Linked List using Extra Memory (Brute Force)"""
    v = []
    # Traverse through the entire linked list and push all the values into the list
    while head is not None:
        v.append(head.data)
        head = head.next
    # Find the middle index
    middleIdx = len(v) // 2
    # Return the value stored at the middle index
    return v[middleIdx]


def find_middle_two_pass(head):
    """Find Middle of the Linked List by Counting Nodes (Two-pass)"""
    # find the len of the linked list
    length = 0
    while head is not None:
        head = head.next
        length += 1
    print(f"length is: {length}")

    # find middle value of the the linked list
    counter = 0
    result = None
    while counter <= length // 2:
        result = head.data
        head = head.next
    return result




head = [None]
# Push nodes into the linked list in reverse order
for i in range(5, 0, -1):
    pushNode(head, i)

# Print the middle value of the linked list
print("Middle Value Of Linked List is :", get_middle_brute_force(head[0]))
