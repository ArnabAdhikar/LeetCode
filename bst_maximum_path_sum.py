# binary tree maximum path sum
# https://www.youtube.com/watch?v=Hr5cWUld4vU

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def maxPathSum(self, root):
        temp = [root.val]
        def dfs(root):
            if root is None:
                return 0
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            
            # we don't want to include the negative values
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)
            
            # compute the max path sum with split
            temp[0] = max(temp[0], leftmax+rightmax+root.data)
            
            # computing the value without split
            return root.val+max(leftmax,rightmax)
        dfs(root)
        return temp[0]
