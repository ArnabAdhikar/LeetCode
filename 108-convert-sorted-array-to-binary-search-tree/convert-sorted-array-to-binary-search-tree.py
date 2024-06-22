# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # recursive solution
        def helper(l, r):
            # base case
            if l > r:
                return None
            # compute the mid
            m = (l+r)//2
            # create the node with the mid first
            root = TreeNode(nums[m])
            # left subtree
            root.left = helper(l, m-1)   # only look at the left of the mid
            root.right = helper(m+1, r)  # only look at the Right of the mid
            return root
        return helper(0, len(nums)-1)
