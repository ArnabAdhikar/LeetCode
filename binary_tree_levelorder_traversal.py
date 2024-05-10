from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        result = []
        count = 0
        def level(count , root):
            if root == None :
                return 
            if len(result) <= count:
                result.append([])    
            result[count].append(root.val)
            count += 1
            level(count , root.left)
            level(count , root.right) 
        level(count , root)
        return result
