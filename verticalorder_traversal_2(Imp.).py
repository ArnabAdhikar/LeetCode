# vertical order traversal Alter(Imp.)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root):
        result = []
        if root is None:
            return result
        cache = {}
        # minimum and maximum column
        self.min1, self.max1=0,0
        def dfs(node, r, c):
            # r = row(appended to the value list) only + starts with 0
            # c = column(key) can be +/-
            if node is None:
                return
            if c in cache:
                cache[c].append([r, node.val])
            else:
                cache[c] = [[r, node.val]]
            self.min1 = min(self.min1, c)
            self.max1 = max(self.max1, c)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
            # after this the dictionary will be ready for use
        dfs(root, 0, 0)
        # now according to the problem we have to arrange the dictionary element
        for c in range(self.min1, self.max1+1):
            # x[0] = row no
            # x[1] = coln. if row no is same
            col = sorted(cache[c], key = lambda x: (x[0], x[1]))
            # extracting value
            finals = []
            for j in col:
                finals.append(j[1]) # value against the key
            result.append(finals)
        return result
