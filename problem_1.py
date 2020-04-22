def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    if target == 1:
        return 1
    if target == 0:
        return 0

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  # integer division in Python 3

        mid_element = array[mid_index]

        if target == mid_element * mid_element:  # we have found the element
            return mid_index

        elif target < mid_element * mid_element:  # the target is less than mid element
            end_index = mid_index - 1  # we will only search in the left half

        else:  # the target is greater than mid element
            start_index = mid_element + 1  # we will search only in the right half

    return -1


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is not int or number < 0:
        return -1

    test_array = range(0, number - 1)

    test_number = binary_search(test_array, number)

    if binary_search(test_array, number) != -1:
        return test_number
    else:
        return -1

#Test cases
print ("Pass" if (3 == sqrt(9)) else "Fail")
print ("Pass" if (0 == sqrt(0)) else "Fail")
print ("Pass" if (4 == sqrt(16)) else "Fail")
print ("Pass" if (2 == sqrt(4)) else "Fail")
print ("Pass" if (1 == sqrt(1)) else "Fail")
print ("Pass" if (5 == sqrt(25)) else "Fail")

#Test cases - no square root
print ("Pass" if (3 != sqrt(10)) else "Fail")
print ("Pass" if (0 != sqrt(8)) else "Fail")
print ("Pass" if (-1 != sqrt(16)) else "Fail")
print ("Pass" if (2 != sqrt(1)) else "Fail")
print ("Pass" if (9 != sqrt(27)) else "Fail")


#edge cases return -1
print(sqrt(None))
print(sqrt(''))
print(sqrt(-1))

