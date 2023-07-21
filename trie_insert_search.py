# Python implementation of Trie
# data structure with insertion
# and search algorithms.
# A Trie (derived from retrieval) is
# a multiway tree data structure used
# for storing strings over an alphabet.
#They are used to store a large amount
# of strrings.Pattern matching is done
# very efficiently using tries.
# The idea is that all strings sharing
# common prefixes should come from a common
# node. Tries are used, for example, in
# spell checking programs.
# A trie is a data structure that supports
#pattern matchin queries in time proportional
# to the pattern size. If we store kets in a
# binary search tree, a well-balanced BST will
# need time proportional to M*log N. Using a
# Trie, they key can be searched in O(M) time.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word


# driver code
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

# Search for words in the Trie
print(trie.search("apple"))  # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("orange"))  # Output: True
print(trie.search("grape"))  # Output: False
