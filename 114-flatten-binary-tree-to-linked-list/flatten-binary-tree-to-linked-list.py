# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # flatten the root tree and return the list tail
        def dfs(root):
            if not root:
                return None
            lefttail = dfs(root.left)
            righttail = dfs(root.right)
            # connecting to the linked list
            if root.left:
                lefttail.right = root.right
                root.right = root.left
                # root node's left subtree is not used
                root.left = None
            # right subtree's non empty tail = entire ll's tail or left.... or root
            last = righttail or lefttail or root
            return last
        dfs(root)
