from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail forward

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


def print_list(head: Optional[ListNode]):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


# Create list1: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create list2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list
print(print_list(merged_list))

# Expected output: [1, 1, 2, 3, 4, 4]
