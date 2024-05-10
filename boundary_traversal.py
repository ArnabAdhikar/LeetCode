# boundary traversal

# Binary tree node class for reference.
# Following is the Binary Tree node structure:

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def leftBoundary(root, ans):
    if(root == None or (root.left == None and root.right == None)):
        return
    ans.append(root.data)
    if(root.left != None):
        leftBoundary(root.left, ans)
    else:
        leftBoundary(root.right, ans)
def traverseLeaf(root,ans):
    if root == None:
        return
    if root.left == None  and root.right== None: 
        ans.append(root.data)
        return  
    traverseLeaf(root.left,ans)
    traverseLeaf(root.right,ans)
def rightBoundary(root, ans):
    if(root == None or (root.left == None and root.right == None)):
        return
    if(root.right != None):
        rightBoundary(root.right, ans)
    else:
        rightBoundary(root.left, ans)
    ans.append(root.data)
def traverseBoundary(root):
    # Write your code here.
    ans =[]
    if root==None:
        return ans  
    ans.append(root.data)
    leftBoundary(root.left,ans)
    traverseLeaf(root.left,ans)
    traverseLeaf(root.right,ans)
    rightBoundary(root.right,ans)
    return ans
