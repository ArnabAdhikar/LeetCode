class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root: BinaryTreeNode) -> int:
    if root is None:
        return 0
    left_height = height(root.left)
    if left_height== -1:
        return -1
    right_height = height(root.right)
    if right_height == -1:
        return -1
    if abs(left_height-right_height)>1:
        return -1
    return max(left_height, right_height)+1
def isBalancedBT(root: BinaryTreeNode) -> bool:
    # Write your code here.
    if height(root)!=-1:
        return True
    else:
        return False
