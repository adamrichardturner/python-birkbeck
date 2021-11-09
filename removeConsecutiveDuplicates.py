def removeConsecutiveDup(nList):
    """
    Write a Python program to remove consecutive duplicates of a given list.

    Params: List

    Returns: List with consecutive duplicates removed.
    """
    # Seen keeps a list of duplicates
    seen = []
    # Clean is our final list representation with duplicates removed
    clean = []
    # For each item in nList..
    for i in nList:
        # If the item has not been seen already...
        if i not in seen:
            # Append the item to clean, our final list
            clean.append(i)
            # Clear seen to remove previous entries
            seen.clear()
            # Append the item to seen
            seen.append(i)
    # Return the duplicates removed here.
    return clean



print(removeConsecutiveDup([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 4, 4])) # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

print(removeConsecutiveDup([])) # returns []

print(removeConsecutiveDup([1])) # returns [1]

print(removeConsecutiveDup([1, 2])) # returns [1, 2]

print(removeConsecutiveDup([1, 1, 2, 2, 2, 2])) # returns [1, 2]