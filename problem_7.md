###Problem 7
Routetrie structure credit to Udacity

###Router Add handler Design
Splits path by slashes
inserts each new subpath into initialized trie

###Time complexity
O(n) - dependent on size of input data - string length of any size

###Space complexity is O(n)
array grows based on size of input string

###Lookup Design
Lookup looks for path in trie
capitalizes and returns name of page

###Time complexity is O(n)
dependent on size of input data

###Space complexity
O(n) doesn't store values, but takes input data of size n