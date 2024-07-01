"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':
        # declaring the pointers
        cur, nxt = node, node.left if node else None
        while cur and nxt:
            cur.left.next = cur.right
            # current's next is not none
            if cur.next:
                cur.right.next = cur.next.left
            # updating the pointer
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return node