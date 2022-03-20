def binary_search_rotate(arr, target, start, end):
    
    if end < start:
        return -1
        
    mid = (end-start+1)//2 + start
    
    if target == arr[mid]:
        return mid
    
    elif target < arr[mid]:
        if target <= arr[end] and arr[mid] > arr[end]:
            return binary_search_rotate(arr, target, mid+1, end)
        else:
            return binary_search_rotate(arr, target, start, mid-1)
        
    else:
        if target >= arr[start] and arr[mid] < arr[start]:
            return binary_search_rotate(arr, target, start, mid-1)
        else:
            return binary_search_rotate(arr, target, mid+1, end)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search_rotate(input_list, number, 0, len(input_list)-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])