# Pair Sum in BST.

def pairSumBST(root, k):
    ans = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        ans.append(root.data)
        inorder(root.right)
    inorder(root)
    i = 0 
    j = len(ans)-1
    while i<j:
        if ans[i]+ans[j] == k:
            return True
        if ans[i]+ans[j] <k:
            i+=1
        else:
            j-=1
    return False
