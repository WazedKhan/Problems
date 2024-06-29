# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next

        return head
