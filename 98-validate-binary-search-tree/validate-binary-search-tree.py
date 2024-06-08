# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # empty binary serach tree is a BST
            if not node:
                return True
            # comparing the node value to the left and the right boundary
            if not(node.val < right and node.val > left):
                return False
            # checking the left and right subtree of node is valid
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
