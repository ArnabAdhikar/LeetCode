# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        dummy = ListNode(0, head)
        # 2 pointers
        prev, cur = dummy, head
        # looping and reversing every pairs of node
        while cur and cur.next:    # need atleast 2 nodes to reverse
            # save pointers
            nextpair = cur.next.next
            second = cur.next

            # reverse this pairs
            second.next = cur
            cur.next = nextpair
            prev.next = second

            # update the pointer
            prev = cur
            cur = nextpair
        return dummy.next
