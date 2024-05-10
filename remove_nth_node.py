# Remove Nth Node From End of List
# https://www.youtube.com/watch?v=XVuQxVej6y8
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1251831419/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0, head)
        # pointers
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n -= 1
        # now shifting both the pointers by 1 untill right reaches the end
        while right:
            left = left.next
            right = right.next
        # deleating the node
        left.next = left.next.next
        # don't include the dummy node
        return dummy.next
