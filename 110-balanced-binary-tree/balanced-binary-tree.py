# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # [ballanced or not?, height of the tree]
        def dfs(root):
            # base case
            if not root:
                return [True, 0]
            # if the left or right sub tree is ballanced?
            left, right = dfs(root.left), dfs(root.right)
            # second value is the Height
            # balanced if left and right is balanced and the height of that node in ballanced position
            balance = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            # also consider the height of the root
            return [balance, 1 + max(left[1], right[1])]
        return dfs(root)[0]
