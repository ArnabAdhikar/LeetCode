# Following is the TreeNode class structure.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def diameterOfBinaryTree(root):
    diameter=0
    def f(root):
        if root==None:
            return 0
        Left=f(root.left)
        Right=f(root.right)
        nonlocal diameter
        diameter=max(diameter,Left+Right)
        # for finfing maximum diameter for all the nodes
        # like a loop's range
        return 1+max(Left,Right)
    f(root)
    return diameter
