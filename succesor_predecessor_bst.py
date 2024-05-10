# predecessor and succesor

'''
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
      
'''
inorder_result = []
def inorder(root):
    if root is not None:
        inorder(root.left)
        inorder_result.append(root.data)
        inorder(root.right)
def predecessorSuccessor(root, key):
    inorder(root)
    finals = [0,0]
	# Write your code here.
    if key not in inorder_result:
        inorder_result.append(key)
        inorder_result.sort()

    ind = inorder_result.index(key)
    if ind==0:
        finals[0]=-1
    else:
        finals[0] = inorder_result[ind-1]
    if ind == len(inorder_result)-1:
        finals[1]=-1
    else:
        finals[1] = inorder_result[ind+1]
    return finals
