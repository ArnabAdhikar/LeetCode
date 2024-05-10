# ceil from BST

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findCeil(root: TreeNode, x):
    # Write your code here.
    ceil = -1
    while root:
        if root.data==x:
            ceil = root.data
            return ceil
        if x<root.data:
            ceil = root.data
            root = root.left
        else:
            root = root.right
    return ceil
