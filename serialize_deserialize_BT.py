# Serialize and Deserialize Binary Tree
# https://www.youtube.com/watch?v=u4JAi2JJhI8&t=3s
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
from logging import root
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            # preorder traversal
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    def deserialize(self, data):
        vals = data.split(",")
        # creating a pointer
        self.i = 0
        def dfs():
            # base case
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            # reconstructing the tree
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
