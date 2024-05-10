# recover BST
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, root, arr):
        if root is None:
            return arr
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    def arr_fix(self, root, v1: int, v2: int) -> None:
        # actual exchange is taking place
        if root is None:
            return
        # edge cases first for recursive calls
        # exchange is taking place between v1 and v2
        if root.val == v1:
            root.val = v2
        elif root.val == v2:
            root.val = v1
        # check for both the branches
        self.arr_fix(root.left, v1, v2)
        self.arr_fix(root.right, v1, v2)
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # atmost 2 positions are wrong
        arr = []
        self.inorder(root, arr)
        actual_arr = sorted(arr)
        # swap is required for 2 places only
        v1 = None
        v2 = None
        for i in range(len(arr)):
            if arr[i]!=actual_arr[i]:
                # lead the value where the problem is if v1 is empty else v2
                if v1==None:
                    v1 = arr[i]
                else:
                    v2 = arr[i]
        self.arr_fix(root, v1, v2)
