def _merge(left, right):
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
        
    # return the ordered, merged list
    return merged

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return _merge(left, right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return None 
    
    # merge sort first
    a = mergesort(input_list)

    return int("".join([str(x) for x in a[0::2]])), int("".join([str(x) for x in a[1::2]]))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    
    solution = test_case[1]
    if output is None and solution is None:
        print("Pass")
    elif sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

        
if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[], None])
    test_function([[1], None])
    test_function([[1, 2], [1,2]])