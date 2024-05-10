# Colone Graph
# https://leetcode.com/problems/clone-graph/description/
# https://www.youtube.com/watch?v=mQeF6bN8hMk


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(node):
            # if the node already in the hash map=> already made clone of it
            if node in old_to_new:
                return old_to_new[node]
            # node not in hashmap
            copy = Node(node.val)
            old_to_new[node] = copy
            # make a copy of every neighbour of the node
            for n in node.neighbors:
                # put this neighbourours as the neighbourours of the copied node
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node) if node else None
