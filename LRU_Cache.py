# LRU Cache
# https://leetcode.com/problems/lru-cache/

class Node:
    # initializing the node
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # hash map, map key to node
        self.cache = {}
        self.cap = capacity
        # dummy nodes
        self.left, self.right = Node(0,0), Node(0,0)
        # left-> Least Recently Used, right-> Most Recently used
        # doubly linked list
        self.left.next, self.right.prev = self.right, self.left
    # insert node at Right
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.next, node.prev = nxt,prev
    # remove from the list
    def remove(self,node):
        # get the pointer
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    def get(self, key: int) -> int:
        # if key exists in cache
        if key in self.cache:
            # after "get"-> edit the usage status=> 1. Remove; 2. Insert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # if key doesn't exists
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # node already exists=> 1. Remove; 2. Insert in cache
            self.remove(self.cache[key])
        # inserting
        self.cache[key] = Node(key, value)
        # doubly ll=> insert this node into our list
        self.insert(self.cache[key])
        # checking for the capacity
        if self.cap==len(self.cache):
            # remove from the list and delete the LRU from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)