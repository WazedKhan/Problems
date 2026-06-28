from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, head: ListNode) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_len = self.length(head=head)
        position = n_len - n
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(position):
            prev = prev.next
        prev.next = prev.next.next

        return dummy.next
