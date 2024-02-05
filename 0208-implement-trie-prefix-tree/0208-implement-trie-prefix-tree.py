class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Returns true if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns true if there is a word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))     # Output: True
print(trie.search("app"))       # Output: False
print(trie.startsWith("app"))   # Output: True
trie.insert("app")
print(trie.search("app"))       # Output: True
