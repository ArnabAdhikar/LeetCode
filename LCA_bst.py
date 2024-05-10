# lowest common ansistor BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        while temp:
            if p.val>temp.val and q.val>temp.val:
                temp = temp.right
            elif p.val<temp.val and q.val<temp.val:
                temp = temp.left
            else:
                # whenever there is a split, the splitting point is the answer
                return temp
