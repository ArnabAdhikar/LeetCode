# top view bianry tree--> 2
# https://www.youtube.com/watch?v=MQyjGCUuj_s

class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    # Write your code here.
    queue= [[root, 0]]
    finals = {}
    while queue:
        node = queue.pop(0)
        cur = node[0]
        data = node[0].val
        coln = node[1]
        if coln not in finals:
            finals[coln] = data
        if cur.left:
            queue.append([cur.left, coln-1])
        if cur.right:
            queue.append([cur.right, coln+1])
    keys = []
    for i in finals.keys():
        keys.append(i)
    keys.sort()
    res = []
    for i in keys:
        res.append(finals[i])
    return res
