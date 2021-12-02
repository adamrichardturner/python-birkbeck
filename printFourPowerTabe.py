def printFourPowerTable(number, power):
    """
    Prints out power tables for a given number.

    Params: number(int), power(int)

    Returns: None, prints a table of values displaying
    every positive value upto number to the power of 
    each positive value upto power.
    """
    # We store our header here...
    header = []
    # Loop upto power + 1, starting at 1...
    for i in range(1, power+1):
        # Append to header x^ + string representation of i
        header.append("x^" + str(i))
    # Print out our header...
    # For i in header (list)...
    for i in header:
        # Print out each item in header with a space of power length...
        print(f'{i:>{power}}', end=' ')
    # Print new line
    print()
    # Print the seperator...
    print("-" * (power + 1) * power)
    # For each i in range upto number + 1...
    for i in range(1, number + 1):
        # Iterate j in range of 1 to power + 1
        for j in range(1, power + 1):
            # Print the values of power for each column...
            print(f'{i ** j:{power}}', end=" ")
        # Print a new line...
        print()

printFourPowerTable(10, 4)