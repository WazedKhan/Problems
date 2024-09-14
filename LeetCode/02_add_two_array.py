from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def list_to_linked_list(self, arr: str) -> ListNode:
        if not arr:
            return ListNode()

        head = ListNode(int(arr[0]))  # Convert the first character to an integer
        current = head

        for item in arr[1:]:
            current.next = ListNode(int(item))  # Convert each character to an integer
            current = current.next

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        step 1: loop through all the nodes from l1 and l2
        step 2: store the value in separated string for both l1 and l2
        step 3: reverse l1 and l2 string and store the sum of them in total_sum: convert str to int before sum
        step 4: convert the total_sum into str and reverse it
        step 5: from the item of total_sum generate a new ListNode return and finally return the Node

        Tags: LinkedList, List, LinkedList-Traversal, List to LinkedList convert
        """

        l1_sum = ""
        l2_sum = ""

        # initializing l1 and l2 stating point
        l1_current = l1
        l2_current = l2

        while l1_current or l2_current:
            if l1_current:
                l1_sum += str(l1_current.val)
                l1_current = l1_current.next

            if l2_current:
                l2_sum += str(l2_current.val)
                l2_current = l2_current.next

        l1_sum = l1_sum[::-1]
        l2_sum = l2_sum[::-1]

        # Sum the two numbers
        total_sum = str(int(l1_sum) + int(l2_sum))
        # Convert the result to a linked list
        return self.list_to_linked_list(total_sum[::-1])

    def print_linked_list(self, linked_list: ListNode):
        current = linked_list
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


# First linked list
node_1 = ListNode(2)
node_1.next = ListNode(4)
node_1.next.next = ListNode(3)

# Second linked list
node_2 = ListNode(5)
node_2.next = ListNode(6)
node_2.next.next = ListNode(4)

solution = Solution()

print("First linked list: ")
solution.print_linked_list(node_1)

print("Second linked list: ")
solution.print_linked_list(node_2)

print("Sum of the two linked lists: ")
sum_list = solution.addTwoNumbers(node_1, node_2)
solution.print_linked_list(sum_list)
