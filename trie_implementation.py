class TrieNode:
    def __init__(self, data=""):
        """
        Purpose: Initializes trie node with data, children, and boolean 
        indicating whether char is end of word.
        """
        self.data = data
        self.children = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        """
        Purpose: Initializes trie with root node.
        """
        self.root = TrieNode("")


    def insert(self, word):
        """
        Purpose: Inserts word into trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                new_node = TrieNode(c)
                node.children[c] = new_node
            node = node.children[c]
        return


    def search(self, word):
        """
        Purpose: Returns whether word exists in trie or not.
        """
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_leaf


    def startsWith(self, prefix):
        """
        Purpose: Returns whether all words start with given prefix.
        """
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True