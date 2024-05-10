# BST deletion

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class solution:
    def smallestDescendant(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root, key):
        if not root:
            return
        else:
            # Checks for Lesser value
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            # Checks for Greater value
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            # Checks if we have reached the node we want to delete
            else:
                # First we check if only 1 child node is present
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    temp = self.smallestDescendant(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
            return root