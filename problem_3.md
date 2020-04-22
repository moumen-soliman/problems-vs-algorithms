### Problem 3

###Mergesort Function Design
divide input array into two arrays
recursively runs mergesort on divided arrays
Reverse merge function checks if values in each array are greater or less than each other and appends each value to merged array
feed arrays into reverse merge functions - reverses array so that the greatest values can be appended to the number slots first so they have the greatest place value in less iterations

###Time complexity
uses O(nlogn) time functions to get array data due to mergesort implementation

###Space Complexity
O(n) - merge sort with a list(array) structure takes up O(n) space

###Rearrange Digits Function Design
run mergesort on input list
calculate length of input list
create sub arrays that are approx half length of main array - if odd number, the first array will have one more number
create arrays by arranging subsequent digits according to their values

###Time complexity 
O(nlogn) - Longest running time based on that of called mergesort

###Space complexity
O(n) - Stored array size dependent on input size, called mergesort is also O(n)