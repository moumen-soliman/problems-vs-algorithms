def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if type(ints) is not list:
        return -1

    smallest = ints[0]
    largest = ints[0]
    for i in ints:
       if i < smallest:
           smallest = i
       if i > largest:
           largest = i

    return (smallest, largest)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

#edge case - fails if string
l2 = "hi"  # a list containing 0 - 9

print ("Pass" if (-1 == get_min_max(l2)) else "Fail") #returns -1

#edge case - fails if string
l3 = None

print ("Pass" if (-1 == get_min_max(l2)) else "Fail") #returns -1