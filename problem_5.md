###Problem 5
Create trie structure - credit to Udacity for tree structure

###Suffixes Design
Return suffixes - loop through all letters, if letter has is_word flag, add to suffix children array
return all suffix children

###Insert Design
Searches for each character in each respective node
Traverses down nodes to correctly insert letters in order

###Find Design
Looks for each character in prefix by traversing through nodes
returns next character if all letters are found in Trie
Otherwise returns not found

###Time complexity
###Suffixes
O(n * m) - loops for each letter in children - recursively dives into children arrays, creating m depth
###Insert
0(n) - loops through input string to insert at bottom of Trie
###Find
O(n) -- loops through input string to find next node after prefix

###Space complexity
###Suffixes
O(n * m) - appends to array for children - recursively dives into children arrays, creating m depth
###Insert and Find
O(n) - storage space dependent on size of string inputs