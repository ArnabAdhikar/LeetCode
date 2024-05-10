# BST search

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def searchInBST(root: TreeNode, x):
    # Write your code here.
    cur = root
    while cur:
        if cur.data==x:
            return True
        elif cur.data>x:
            cur=cur.left
        else:
            cur=cur.right
    return False
