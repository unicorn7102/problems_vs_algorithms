def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) < 1:
        return (None, None)
    
    minimum, maximum = ints[0], ints[0]
    for i in range(1, len(ints)):
        current = ints[i]
        if current < minimum: 
            minimum = current
        if current > maximum:
            maximum = current
    return (minimum, maximum)

def test_function(l):
    if l is None or len(l) < 1:
        print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")
    else:
        print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")

        
if __name__ == "__main__":
    import random

    l = [i for i in range(0, 10)]
    random.shuffle(l)

    test_function(l)
    test_function([1])
    test_function([])
    test_function(None)

