# min val from BST

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
def minVal(root: Node):
    # Write your code here.
    cur = root
    if root is None:
        return -1
    while cur.left is not None:
        cur=cur.left
    return cur.data
