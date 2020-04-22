def find_minimum(input_list):

    start_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  # integer division in Python 3

        mid_element = input_list[mid_index]

        if input_list[mid_index - 1] > mid_element:
            new_start_index = mid_index
            break

        elif input_list[mid_index + 1] < mid_element:  # the target is less than mid element
            new_start_index = mid_index + 1  # we will only search in the left half
            break

        elif mid_element < input_list[end_index]:
            end_index = mid_index

        else:  # the target is greater than mid element
            start_index = mid_element + 1  # we will search only in the right half

    return new_start_index


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if type(number) != int:
        return -1

    if type(input_list) != list or len(input_list) == 0:
        return -1

    start_index = 0
    end_index = len(input_list) - 1

    new_start_index = find_minimum(input_list)

    if input_list[new_start_index] == number:
        return new_start_index
    elif input_list[0] == number:
        return 0
    elif input_list[0] < number:
        end_index = new_start_index - 1
        mid_index = (start_index + end_index) // 2
        mid_element = input_list[mid_index]

        while start_index < end_index:

            if mid_element == number:
                return mid_index
            elif mid_element > number:
                end_index = mid_index - 1
            elif mid_element < number:
                start_index = mid_index + 1

        #checks last element if start and end indexes match
        if start_index == end_index and input_list[start_index] == number:
            return start_index

    elif input_list[0] > number:

        start_index = new_start_index + 1
        mid_index = (start_index + end_index) // 2
        mid_element = input_list[mid_index]

        while start_index < end_index:
            if mid_element == number:
                return mid_index
            elif mid_element > number:
                end_index = mid_index - 1
            elif mid_element < number:
                start_index = mid_index + 1

        #checks last element if start and end indexes match
        if start_index == end_index and input_list[start_index] == number:
            return start_index
    else:
        return -1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print(linear_search(input_list, number))
        print("Pass")
    else:
        print("Fail")

#test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #returns 0 pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #returns 5 pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #returns 2 pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #returns 3 pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #returns -1 pass

#edge cases
test_function([[6, 10, 8, 1, 2, 3, 4], None]) #returns -1 pass
test_function([[6, 10, 8, 1, 2, 3, 4], []]) #returns -1 Pass
test_function([[], 1]) #returns Insufficient input