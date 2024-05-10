# Reorder List
# https://www.youtube.com/watch?v=S5bfdUTrKLM
# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding the middle point of the list
        slow, fast = head, head.next
        # shifting the pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # second half of the list
        second = slow.next
        prev = slow.next = None
        # changing the link in the second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merge the 2 halves
        first, second = head, prev
        # second part will always smaller
        while second:
            # before modification store the link
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            # shift the pointers
            first, second = temp1, temp2
