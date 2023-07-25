# Python program to delete a key from
# a Trie (pronounced Try) data structure.
# A Trie is a mutltiway tree data structure
# used for storing strings over an alphabet.
# In a previously posted program, I described
#and implemented a program to insert and search
# in a Trie. This algorithm deletes a node
# from the Trie. The following four possible
#conditions arise when deleting from a Trie.
# 1) Key may not be in the trie. Delete operation
# should not modify the tree.
# 2) Key may be present as unique key (no part of
#the key contains another key (prefix), nor the key
#itself is a prefix if another key). In this case,
# delete all nodes
# 3) Key is prefix if another long key in trie.
# We unmark the leaf node.
# 4) Key is present in trie and has at least
#one other key as prefix key. In this case, delete
#nodes from the end of key until first leaf node
# of longest prefix key.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def delete(self, word):
        def delete_helper(node, word, index):
            if index == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    if not node.children:
                        return True
                return False
            char = word[index]
            if char in node.children:
                if delete_helper(node.children[char], word, index + 1):
                    del node.children[char]
                    return not node.is_end_of_word and not node.children
            return False

        delete_helper(self.root, word, 0)

    def display(self):
        def display_helper(node, prefix):
            if node.is_end_of_word:
                print(prefix)
            for char, child in node.children.items():
                display_helper(child, prefix + char)

        display_helper(self.root, "")

# Testing the Trie
trie = Trie()
words = ["apple", "banana", "applesauce", "orange"]
for word in words:
    trie.insert(word)

print("Before deletion:")
trie.display()

word_to_delete = "apple"
trie.delete(word_to_delete)

print("\nAfter deleting: '{}'".format(word_to_delete))
trie.display()
