# binary search tree

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def createnode(self, data):
        return TreeNode(data)
    def insert(self, current_node, data):
        if current_node is None:
            return self.createnode(data)
        elif data < current_node.data:
            current_node.left = self.insert(current_node.left, data)
        else:
            current_node.right = self.insert(current_node.right, data)
        return current_node
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

# driver code
tree = Tree()
root = tree.createnode(5)
print(root.data)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)
print("Inorder-->")
tree.inorder(root)
