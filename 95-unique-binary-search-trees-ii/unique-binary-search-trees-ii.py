# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right):
            # only 1 node
            if left == right:
                return [TreeNode(left)]
            # range is empty
            if left > right:
                return [None]
            # building the list for trees
            res = []
            for val in range(left, right + 1):
                # we need every combination of the subtrees

                # construct the left subtree
                for lefttree in generate(left, val-1):
                    # construct the right subtree
                    for righttree in generate(val+1, right):
                        root = TreeNode(val, lefttree, righttree)
                        res.append(root)
            return res
        return generate(1, n)
