# BST iterator

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []
        self.current_pointer = 0
        self.inorder(root)

    def inorder(self, node: TreeNode):
        if node is None:
            return
        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        # Moves the pointer to the right, then returns the number at the pointer
        val = self.arr[self.current_pointer]
        self.current_pointer+=1
        return val

    def hasNext(self) -> bool:
        # Returns true if there exists a number in the traversal to the right of the pointer
        if self.current_pointer<=len(self.arr)-1:
            return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
