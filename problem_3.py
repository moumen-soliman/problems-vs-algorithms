def mergesort(input_list):
    if type(input_list) is not list:
        return -1

    if len(input_list) <= 1:
        return input_list

    midpoint = len(input_list) // 2
    left = input_list[:midpoint]
    right = input_list[midpoint:]

    left = mergesort(left)
    right = mergesort(right)

    return reverse_merge(left, right)


def reverse_merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #input_list.sort(reverse=True)

    if type(input_list) is not list:
        return -1

    input_list = mergesort(input_list)
    print(input_list)

    #create sub arrays that are approx half length of main array - if odd number, the first array will have one more number
    array_length = len(input_list)
    if len(input_list) % 2 == 1:
        first_number_digits = int(array_length / 2) + 1
    else:
        first_number_digits = int(array_length / 2)

    second_number_digits = array_length - first_number_digits
    first_half_array = [-1 for i in range(first_number_digits)]
    second_half_array = [-1 for i in range(second_number_digits)]

    # create state tracker to alternate adding numbers from input array into new shorter arrays
    first_array = True

    first_number_insert_slot = first_number_digits - 1
    second_number_insert_slot = second_number_digits - 1

    #add numbers to arrays
    for number in input_list:
        if first_array:
            first_half_array[first_number_insert_slot] = number
            first_number_insert_slot -= 1
            first_array = False
        else:
            second_half_array[second_number_insert_slot] = number
            second_number_insert_slot -= 1
            first_array = True

    #add numbers from each array to output numbers using place in array to square for appropriate place value
    first_number = 0
    second_number = 0

    for i in range(first_number_digits):
        first_number += first_half_array[i] * 10**i

    for i in range(second_number_digits):
        second_number += second_half_array[i] * 10**i

    return [first_number, second_number]

print(rearrange_digits([1, 2, 3, 4, 5]))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if output is not -1:
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[4, 6, 2, 5, 8, 8], [864, 852]]
test_case3 = [[4, 6, 2, 5, 8, 8, 4], [854, 8642]]
test_function(test_case)
test_function(test_case2)
test_function(test_case3)

#edge cases
test_case4 = [0, [0]] #Fail - first input is not an array
test_function(test_case4)
test_case5 = [None, [0]] #Fail - first input is not an array
test_function(test_case5)