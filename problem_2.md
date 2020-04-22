###Problem 2

###Find minimum function design
looks for smallest value in array
Initalizes start index to search
Initalize end index
create while loop that runs until start index reaches end index
creates mid index
grabs mid element
checks if element is greater or less than elements next to it
reassigns start index to half the array - binary search

###Time Complexity
O(logN) - Binary searches to find minimum value

###Space Complexity
O(1) - two variables are initialized through entire function

### Rotated Array Search Function Design
Searches rotated array for given number in given input list
initializes start and end indices
uses find minimum to get rotated start index in order to divide array into two subarrays with binary search structure
If number matches new start index, return the new start index
If number matches number at input 0 - return 0
If 0 input is less than number, then check first part of array
If 0 input is greater than number, then check second part of array

###Time Complexity
O(logN) - Dependent on binary search output

###Space complexity
O(1) - single variables allocated to hold values - size not dependent on input