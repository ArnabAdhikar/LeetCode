# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# https://www.youtube.com/watch?v=oobqoCJlHA0&t=1s

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
        # children["a"] = TrieNode()
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # if this character is not in our hash map yet
            if c not in cur.children:
                # insert
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # mark the ending of the word
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            # if the character exists in our tree
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
