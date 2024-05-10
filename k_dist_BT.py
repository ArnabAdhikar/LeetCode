# All Nodes Distance K in Binary Tree
# https://www.youtube.com/watch?v=2IHdqU48N2w&t=9s
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

import collections
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # if k = 0
        if not k:
            return [target.val]
        # else build a graph
        graph = collections.defaultdict(list)
        # to build this graph, use a queue
        queue = collections.deque([root])
        # process the tree
        while queue:
            node = queue.popleft()
            if node.left:
                # put it into the graph (bidirectional connections)
                graph[node].append(node.left)
                graph[node.left].append(node)
                # put the node in the queue for processing
                queue.append(node.left)
            if node.right:
                # put it into the graph (bidirectional connections)
                graph[node].append(node.right)
                graph[node.right].append(node)
                # put the node in the queue for processing
                queue.append(node.right)
        res = []
        # track the visited node=> eleminate the infinite loop
        visited_set = set([target])   # target=> starting point
        # BFS
        # queue is initialized with a tuple (target, step count)
        queue = collections.deque([(target, 0)])
        while queue:
            node, steps = queue.popleft()
            if steps == k:
                res.append(node.val)
            else:
                # visit all the other point that we can visit from that point
                for i in graph[node]:
                    # nodes which we have not visited previousely
                    if i not in visited_set:
                        visited_set.add(i)
                        queue.append((i, steps+1))
        return res
