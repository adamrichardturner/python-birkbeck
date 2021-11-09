def altSum(numList):
    """
    Function that calculates and returns the alternating sum of all elements in a list.
    E.G For example, if the list is [1, 4, 9, 16, 9, 7, 4, 9, 11], then it computes
    1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = -2

    Params: numList(list of nums)

    Returns: The computation of the alternating sum.
    """
    # Storing the total of computation here.
    altTotal = 0
    # Enumerate the list 
    for index, num in enumerate(numList):
        # If the index is even...
        if index % 2 == 0:
            # We add the number to altTotal
            altTotal += num
        else:
            # If not even, we minus the number from altTotal
            altTotal -= num
    # Return altTotal
    return altTotal

# Test Cases
print(altSum([])) # 0
print(altSum([4])) # 4
print(altSum([3, -8])) # 11
print(altSum([1, 4, 9, 16, 9, 7, 4, 9, 11])) # -2