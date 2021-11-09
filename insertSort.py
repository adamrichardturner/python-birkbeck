def sortInsert(sortedIntList, newInt):
    """
    Function that insets a new value newInt into its proper position without calling
    the sort function. E.G

    sortedIntList is [2, 6, 9, 19]

    newInt is 16

    updated sortedIntList is [2, 6, 9, 16, 19]

    Params: sortedIntList(list), newInt(integer)

    Returns: List sorted with the integer in the correct place 
    """
    # For each index and number in enumerated sortedIntList...
    for i, n in enumerate(sortedIntList):
        # If the newInt is less than the number being iterated
        if newInt < n:
            # We inset newInt at the index of i
            sortedIntList.insert(i, newInt)
            # Return the sortedIntList
            return sortedIntList
    # Append the newInt to the list if it is greater than all numbers
    sortedIntList.append(newInt)
    # Return the sortedIntList now modified
    return sortedIntList

print(sortInsert([0,2,4,6], 0)) # Returns [0, 0, 2, 4, 6]
print(sortInsert([0,2,4,6], 1)) # Returns [0, 1, 2, 4, 6]
print(sortInsert([0,2,4,6], 3)) # Returns [0, 2, 3, 4, 6]
print(sortInsert([0,2,4,6], 4)) # Returns [0, 2, 4, 4, 6]
print(sortInsert([0,2,4,6], 6)) # Returns [0, 2, 4, 6, 6]
print(sortInsert([0,2,4,6], 7)) # Returns [0, 2, 4, 6, 7]