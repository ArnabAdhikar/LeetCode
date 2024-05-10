# Subtree of Another Tree
# https://www.youtube.com/watch?v=E36O5SWp-LE
# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False
        if self.sametree(s, t):
            return True
        # return true if t is the sub tree of left of s or t is the sub tree of right of s
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))
    def sametree(self, s, t):
        # both the tree is empty
        if not s and not t:
            return True
        # bith the trees are non null and with same root value
        if s and t and s.val == t.val:
            # checking for the left and right sub tree and return true if both of them are equal 
            return (self.sametree(s.left, t.left) and
                    self.sametree(s.right, t.right))
        # if 1 of them is empty and 1 of them is non empty
        return False
