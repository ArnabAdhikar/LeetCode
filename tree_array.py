# tree creation using an array

from typing import List

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def insertion(arr: List[int], pos):
    if pos<len(arr):
        newnode = Node(arr[pos])
        # odd position element
        newnode.left = insertion(arr, 2*pos+1)
        # even position element
        newnode.right = insertion(arr, 2*pos+2)
        return newnode
    return None
def createTree(arr: List[int]) -> Node:
    # Write your code here.
    if len(arr)==0:
        return None
    return insertion(arr, 0)
