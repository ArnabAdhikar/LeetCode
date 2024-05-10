# count complete tree node
# https://www.youtube.com/watch?v=i_r2uKbwHCU
# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right, left = root, root
        left_height, right_height = 0, 0
        while left!= None:
            left_height += 1
            left = left.left
        while right!= None:
            right_height += 1
            right = right.right
        if left_height == right_height:
            return (1<<left_height)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
