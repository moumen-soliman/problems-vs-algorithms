In this problem I am supposed to implement the search algorithm in the rotated sorted array. As I have to find the given number and I have to do it in log(n) time.
Solution which come to my mind is binary search but the given array is not sorted array, but rotated sorted array. So, to find the pivot from where it is rotated is I have found the pivot first i.e. by how much amount the sorted array is shifted.
Then in the two divided part I have implemented the binary search directly.

Time Complexity: O(log(n))
Space Complexity: O(1)
