# https://leetcode.com/problems/accounts-merge/description
# https://youtu.be/FXWRE67PLL0?si=HivjXxvvBnJ63Exv
"""
Created on Mon Feb 12 22:47:04 2024

@author: ARNAB ADHIKARY
"""
from collections import defaultdict
from typing import List
class Unionfind:
    def __init__(self, edges):
        # initializing the parent and the rank
        self.parent = [i for i in range(edges)]
        self.rank = [1]*edges
    def find(self, node):
        # finding the last root parent
        while node!=self.parent[node]:
            # link compression
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self, node1, node2):
        # finding the parent of 2 nodes
        p1, p2 = self.find(node1), self.find(node2)
        if p1==p2:
            # same parent cycle encountered
            return False
            # unioning them
        if self.rank[p1] > self.rank[p2]:
            # p1 is the parent of p2
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Unionfind(len(accounts))
        # e-mail-> index of account
        eindex = {}
        for i, a in enumerate(accounts):
            # first value of a = Name(skip that)
            for e in a[1:]:
                # if email already exists in the hashmap
                if e in eindex:
                    # these 2 accounts should be unioned together
                    uf.union(i, eindex[e])
                # doesnt exists
                else:
                    eindex[e] = i
        # every email should belong to single account
        egroup = defaultdict(list)  # index of account-> list of emails
        for e, i in eindex.items():
            # finding the emails with same leaders
            leader = uf.find(i)
            egroup[leader].append(e)
        # outut
        ans = []
        for i, emails in egroup.items():
            name = [accounts[i][0]]
            name.extend(sorted(emails))
            ans.append(name)
        return ans
