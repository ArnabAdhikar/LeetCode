# is BST or not

from sys import stdin
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
INT_MIN = -2147483648
INT_MAX = 2147483647
############## MAIN CODE #############################################################################
def isBST(root):
    # Write your code here
    def is_valid(root, left, right):
        if root is None:
            return True
        # if root data is less than the right and
        # if root data is greater than the left ==> BST
        if not (root.data>left and root.data<right):
            return False
        # check the same for the left subtree and the right sub tree
        # left subtree-> update right
        # right subtree-> update left
        return (is_valid(root.left, left, root.data) and is_valid(root.right, root.data, right))
    # initilally the root node between -infiniy to +infinity
    return is_valid(root, INT_MIN, INT_MAX)
######################################################################################################
#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main

root = takeInput()
print('true') if isBST(root) else print('false')