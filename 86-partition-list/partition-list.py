# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # left and right pointer pointing to the dummy nodes
        left, right = ListNode(), ListNode()
        left_tail, right_tail = left, right
        while head:
            if head.val < x:
                left_tail.next = head
                # update the tail
                left_tail = left_tail.next
            else:
                right_tail.next = head
                # update the tail
                right_tail = right_tail.next
            head = head.next
        # updating the links
        left_tail.next = right.next
        right_tail.next = None
        return left.next
