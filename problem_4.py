def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if type(input_list) is not list:
        print("Warning: invalid input")
        return -1

    zero_index = 0
    current_index = 0
    two_index = len(input_list) - 1

    while current_index <= two_index:
        if input_list[current_index] == 0:
            input_list[current_index], input_list[zero_index] = input_list[zero_index], input_list[current_index]
            zero_index += 1
            current_index += 1
        elif input_list[current_index] == 2:
            input_list[current_index], input_list[two_index] = input_list[two_index], input_list[current_index]
            two_index -= 1
        else:
            current_index += 1

    return input_list


def test_function(test_case):
    if type(test_case) is not list:
        print("Fail")
        return
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 3]) #Fails - wrong item in array
test_function(0) #Fails - wrong item in array