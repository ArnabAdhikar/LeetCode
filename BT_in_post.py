# Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# https://www.youtube.com/watch?v=vm63HuIU7kw

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
from altair import Optional
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        # creating the root node
        root = TreeNode(postorder.pop())
        # finding the index of the root value in the inorder list
        indx = inorder.index(root.val)
        # building the right sub tree
        root.right = self.buildTree(inorder[indx+1:], postorder)  # postorder array will be the same
        # building the left sub tree
        root.left = self.buildTree(inorder[:indx], postorder)
        return root
