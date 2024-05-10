# Maximum Width of Binary Tree
# https://www.youtube.com/watch?v=FPzLE2L7uHs
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # initializing the queue, passing the initial tuple => [node, num, level]
        q = deque([[root, 1, 0]])
        prevlevel, prevnum = 0, 1
        while q:
            # num -> current number
            node, num, level = q.popleft()
            # keeping track of the level
            if level>prevlevel:
                prevlevel = level
                # update the previous no with the 1st no of the same level
                prevnum = num
            # main operation
            res = max(res, num-prevnum+1)
            # enqueue the non null children in left to right format
            if node.left!=None:
                # left child value weplaced with (2*num)
                q.append([node.left, 2*num, level+1])
            if node.right!=None:
                # left child value weplaced with (2*num)
                q.append([node.right, 2*num+1, level+1])
        return res
