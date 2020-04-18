Note - I have added the files with all the easy extensions. Feel free to check anyone.

In this problem, I have to implement a Trie, which is a tree like structure that stores a dynamic set of strings.
Here first I have made a class for TrieNode which has insert & suffixes methods.
Trie class is made with the insert word & find methods.

Talking about the complexity of this data structure:

TrieNode:

Insert a character:
Time complexity - O(1)
Space complexity - O(1)

suffixes of a node:
Time complexity: O(m^n)
Space complexity: O(m^n)
where m is maximum number of elements one level can have & n is the number of levels.

Trie:

Insert a word:
Time complexity: O(n)
Space complexity: O(n)

Find a prefix:
Time complexity: O(n)
Space complexity: O(1)
