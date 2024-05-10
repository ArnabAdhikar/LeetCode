# Lowest common ansistor of Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://www.youtube.com/watch?v=gs2LMfuOR9k

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # start from the root node
        cur = root
        # start scanning from top to the bottom
        while cur:
            # p and q are both greater than the root value => Right
            if p.val>cur.val and q.val>cur.val:
                cur = cur.right
            # p and q are both smaller than the root value => Right
            elif p.val<cur.val and q.val<cur.val:
                cur = cur.left
            # if split occurs => found the required value
            else:
                return cur
