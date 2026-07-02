from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        slow.next = None

        prev = None
        while half:
            next_node = half.next
            half.next = prev
            prev = half
            half = next_node

        while head and prev:
            next_head = head.next
            head.next = prev
            next_prev = prev.next
            prev.next = next_head
            head = next_head
            prev = next_prev
