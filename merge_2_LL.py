# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# https://www.youtube.com/watch?v=XIdigk956u0&t=2s

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create dummy node
        dummy = ListNode()
        # pointer
        tail = dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # update the tail node regardless
            tail = tail.next
        # if one is empty and other is non empty
        if l1:
            # taking the remaining portion of fl and inserting to the result
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
