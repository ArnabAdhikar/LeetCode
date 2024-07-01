# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetsum: int) -> bool:
        # Inorder DFS
        def dfs(node, cursum):
            # Base case
            if not node:
                return False
            cursum += node.val
            # checking for the result => leaf node
            if not node.left and not node.right:
                return cursum == targetsum
            return (dfs(node.left, cursum) or 
                    dfs(node.right, cursum))
        return dfs(root, 0)
