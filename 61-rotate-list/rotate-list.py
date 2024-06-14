# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # empty ll
        if not head:
            return head
        # get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        # no of rotation is the multiple of the length of the ll
        k = k % length
        if k == 0:
            return head
        # move the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        # store the new head
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead
