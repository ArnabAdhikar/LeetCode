"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hash map
        oldtocopy = {None : None}
        # iterating the current linked list
        cur = head
        while cur:
            # deep copying the node
            copy = Node(cur.val)
            # put the copy into the hash map
            oldtocopy[cur] = copy
            # update the current pointer
            cur = cur.next
        # connecting the list
        cur = head
        while cur:
            # set the pointers
            copy = oldtocopy[cur]
            copy.next = oldtocopy[cur.next]
            copy.random = oldtocopy[cur.random]
            cur = cur.next
        # return the head
        return oldtocopy[head]
