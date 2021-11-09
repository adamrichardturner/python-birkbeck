def listDifference(list1, list2):
    """
    Compares list1 with list2 returning the items that are different in list1 against
    list 2.

    Params: list1(list), list2(list)

    Returns: The items that are different in list 1 (not in list 2)
    """
    # We will keep our different items here.
    listDiff = []
    # For each item in list1...
    for item in list1:
        # If that item is not in list2...
        if item not in list2:
            # Append that different item to the listDiff list.
            listDiff.append(item)
    # Return the listDifference
    return listDiff

# Run the two test cases and print out the results
colour1 = ["red", "orange", "green", "blue", "white"]
colour2 = ["black", "yellow", "green", "blue"]

print(listDifference(colour1, colour2)) # ['red', 'orange', 'white']
print(listDifference(colour2, colour1)) # ['black', 'yellow']

list1 = []
list2 = [1, 2]

print(listDifference(list1, list2)) # []
print(listDifference(list2, list1)) # [1, 2]