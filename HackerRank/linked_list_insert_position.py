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


def push_at(self, newElement, position):

    # 1. allocate node to new element
    newNode = Node(newElement)

    # 2. check if the position is > 0
    if position < 1:
        print("\nposition should be >= 1.")
    elif position == 1:

        # 3. if the position is 1, make next of the
        #   new node as head and new node as head
        newNode.next = self.head
        self.head = newNode
    else:

        # 4. Else, make a temp node and traverse to the
        #   node previous to the position
        temp = self.head
        for i in range(1, position - 1):
            if temp != None:
                temp = temp.next

        # 5. If the previous node is not null, make
        #   newNode next as temp next and temp next
        #   as newNode.
        if temp != None:
            newNode.next = temp.next
            temp.next = newNode
        else:

            # 6. When the previous node is null
            print("\nThe previous node is null.")


# Python3 program for insertion in a single linked
# list at a specified position


# A linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


# function to create and return a Node
def getNode(data):

    # allocating space
    newNode = Node(data)
    return newNode


# function to insert a Node at required position
def insertPos(headNode, position, data):
    head = headNode

    # This condition to check whether the
    # position given is valid or not.
    if position < 1:
        print("Invalid position!")

    if position == 1:
        newNode = Node(data)
        newNode.nextNode = headNode
        head = newNode

    else:

        # Keep looping until the position is zero
        while position != 0:
            position -= 1

            if position == 1:

                # adding Node at required position
                newNode = getNode(data)

                # Making the new Node to point to
                # the old Node at the same position
                newNode.nextNode = headNode.nextNode

                # Replacing headNode with new Node
                # to the old Node to point to the new Node
                headNode.nextNode = newNode
                break

            headNode = headNode.nextNode
            if headNode == None:
                break
        if position != 1:
            print("position out of range")
    return head


# This function prints contents
# of the linked list
def printList(head):
    while head != None:
        print(" " + str(head.data), end="")
        head = head.nextNode
    print()


# Driver Code
if __name__ == "__main__":

    # Creating the list 3.5.8.10
    head = getNode(3)
    head.nextNode = getNode(5)
    head.nextNode.nextNode = getNode(8)
    head.nextNode.nextNode.nextNode = getNode(10)
    print("Linked list before insertion: ", end="")
    printList(head)
    data = 12
    position = 3
    head = insertPos(head, position, data)
    print("Linked list after insertion of 12 at position 3: ", end="")
    printList(head)

    # front of the linked list
    data = 1
    position = 1
    head = insertPos(head, position, data)
    print("Linked list after insertion of 1 at position 1: ", end="")
    printList(head)

    # insertion at end of the linked list
    data = 15
    position = 7
    head = insertPos(head, position, data)
    print("Linked list after insertion of 15 at position 7: ", end="")
    printList(head)

# This code iscontributed by rutvik_56
