## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix='', word_comp='', suffix_children=[]):
        ## Recursive function that collects the suffix for
        ## all complete words below this point

        if suffix not in self.children:
            return -1

        for letter in self.children[suffix].children:
            word_comp = word_comp + letter
            if self.children[suffix].children[letter].is_word == True:
                suffix_children.append(word_comp)
            self.children[suffix].suffixes(letter, word_comp, suffix_children)
            word_comp = ""

        return suffix_children

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
                current_node = current_node.children[char]
            else:
                current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                print('Not found')
                return

        return current_node.children.keys()


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.root.suffixes('f'))
print(MyTrie.find('factor')) #returns ['y']
print(MyTrie.find('facto')) #returns ['r']
print(MyTrie.find('factorie')) #returns Not found

#Edge Case
MyTrie2 = Trie()

wordList2 = [
    "ant", "anthology", "antagonist", "antonym",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList2:
    MyTrie2.insert(word)

print(MyTrie2.root.suffixes('f')) #f not in trie - return -1

#Edge Case
MyTrie2 = Trie()

wordList2 = [
    "ant", "anthology", "antagonist", "antonym",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList2:
    MyTrie2.insert(word)

print(MyTrie2.root.suffixes(None)) #None not in trie - return -1

