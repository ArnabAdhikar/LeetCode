# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        answer = []
        def dfs(root, level, answer):
            if root is None:
                return
            if len(answer)<=level:
                # for every level we should have a new list
                answer += [[]]
            dfs(root.left, level+1, answer)
            dfs(root.right, level+1, answer)
            # even level-> Append
            if level%2==0:
                # value should be appended to ins level's list
                answer[level].append(root.val)
            # odd level-> prepend
            else:
                answer[level].insert(0, root.val)
        dfs(root, 0, answer)
        return answer
