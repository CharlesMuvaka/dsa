def linear_search(list1, target):
    """
    Returns the index of the target if found in the list
    """
    for i in range(0, len(list1)):
        if list1[i] == target:
            return i
    return None


def binary_search(list2, target):
    first_index = 0
    last_index = len(list2) - 1

    while first_index <= last_index:
        mid_point = (first_index + last_index) // 2
        if target == list2[mid_point]:
            return mid_point
        elif list2[mid_point] < target:
            first_index = mid_point + 1
        else:
            last_index = mid_point - 1
    return None


def binary_recursive_search(list3, target):
    if len(list3) == 0:
        return False
    else:
        mid_point = len(list3) // 2
        if list3[mid_point] == target:
            return True
        else:
            if list3[mid_point] < target:
                return binary_recursive_search(list3[mid_point + 1:], target)
            else:
                return binary_recursive_search(list3[:mid_point], target)


def verify(index):
    if index is not None:
        print("Index found at is: ", index)
    else:
        print("number not in list")


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = linear_search(numbers, 10)
    result2 = binary_search(numbers, 1)
    result1 = binary_recursive_search(numbers, 15)
    # verify(result1)
    print(result1)
