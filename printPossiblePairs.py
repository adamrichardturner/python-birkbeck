def printPossiblePairs(n):
    """
    Prints all possible pairs of positive numbers from 1 upto n on rows
    of n length.

    Params: n(int)

    Returns: None, prints rows of possible number combinations from 1 upto
    n.
    """
    # For each index in range from 1 to n + 1...
    for i in range(1, n + 1):
        # Inner loop iterates the same on each iteration of outer loop.
        for j in range(1, n + 1):
            # If j == n we print the last pair and a space...
            if j == n:
                print(f'({i},{j})', end="")
                print()
            # Else we just print the pair...
            else:
                print(f'({i},{j})', end="")
            
printPossiblePairs(0)
printPossiblePairs(1)
printPossiblePairs(2)
printPossiblePairs(4)