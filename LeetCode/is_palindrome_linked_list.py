from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self, head: Optional[ListNode]):
        pass

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass

    def is_palindrome_str(self, head: Optional[ListNode]) -> bool:
        current = head
        temp_str = ""
        while current is not None:
            temp_str += str(current.val)
            current = current.next
        return temp_str == temp_str[::-1]

    def insert_from_list(self, head: Optional[ListNode], values: List[int]) -> Optional[ListNode]:
        if not values:
            return None

        head.val = values[0]
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        return head

    def print_linked_list(self, head: Optional[ListNode]):
        current = head
        while current is not None:
            print(current.val, end=" => " if current.next else " \n")
            current = current.next


values = [1, 2, 2, 1]
head = ListNode()  # Initialize an empty node to serve as the head
head = Solution().insert_from_list(head=head, values=values)
Solution().print_linked_list(head=head)
print(Solution().is_palindrome_str(head=head))
# Expected Output: 1 -> 2 -> 2 -> 1
