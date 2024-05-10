# vertical order traversal Alter(Imp.)

# Definition for a binary tree node.
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

# the main problem logic
def getTopView(root):
    dick = {}
    result = []
    # traversing all the nodes
    def traversal(root, key, level):
        if root:
            # key not present in the dictionary
            if key not in dick:
                dick[key] = [root, level]
            # key with lesser level
            elif dick[key][1] > level:
                dick[key] = [root, level]
            # traverse the left and the right
            traversal(root.left, key-1, level+1)
            traversal(root.right, key+1, level+1)
    traversal(root, 0, 0)
    for i in sorted(dick):
        # append the main value not the node
        result.append(dick[i][0].data)
    return result
######################################################

# Taking input.
def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))
    rootData = arr[0]
    n = len(arr)
    if(rootData == -1):
        return None
    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()
        leftChild = arr[index]
        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        index += 1
        rightChild = arr[index]
        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)
        index += 1
    return root
# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()
# Main.
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getTopView(root)

    printAns(ans)
