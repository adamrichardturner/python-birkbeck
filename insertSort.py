def sortInsert(sortedIntList, newInt):
    for i, n in enumerate(sortedIntList):
        if newInt < n:
            sortedIntList.insert(i, newInt)
            return sortedIntList
    sortedIntList.append(newInt)
    return sortedIntList

print(sortInsert([2, 6, 9, 19], 0))