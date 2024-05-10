# Right View BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if root is None:
            return
        q = [root]
        values = []
        while q:
            level_values = []
            for i in range(len(q)):
                node = q.pop(0)
                level_values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            values.append(level_values)
        finals = []
        for i in range (len(values)):
            finals.append(values[i][-1])
        return finals
