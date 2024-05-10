# height of binary tree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    # Write your code here.
    if root is None:
        return 0
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)
    return 1+max(left_height, right_height)
