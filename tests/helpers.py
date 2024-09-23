from typing import List
from LeetCode.is_palindrome_linked_list import ListNode

# Helper function to convert list to linked list (for easy setup in test cases)
def list_to_linked_list(arr: List[int]):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head