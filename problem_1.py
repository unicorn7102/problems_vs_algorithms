def binary_search_sqrt(arr, target_squared, start, end):
    
    if end == start or end == start + 1:
        if arr[end]**2 == target_squared: 
            return arr[end]
        else:
            return arr[start]
    
    mid = (end-start+1) // 2 + start
    #print(start, end, mid)
    if arr[mid]**2 == target_squared:
        return arr[mid]
    elif arr[mid]**2 > target_squared:
        return binary_search_sqrt(arr, target_squared, start, mid-1)
    else:
        return binary_search_sqrt(arr, target_squared, mid, end)
    
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return None
    
    arr = list(range(number+1))
    return binary_search_sqrt(arr, number, 0, number)

if __name__ == "__main__":
    
    print ("Pass" if  (None == sqrt(None)) else "Fail")
    print ("Pass" if  (None == sqrt(-1)) else "Fail")
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")