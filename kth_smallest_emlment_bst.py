# kth smallest element in a tree

from typing import Optional

class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None
inorder_result = []
def inorder(root):
    if root is not None:
        inorder(root.left)
        inorder_result.append(root.data)
        inorder(root.right)
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    
    # Write the code here.
    inorder(root)
    return inorder_result[k-1]
