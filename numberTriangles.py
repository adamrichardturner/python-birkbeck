def numberTriangle(start, step, height):
    """
    Returns a number triangle based on start, step and height values.

    Params: start(int), step(int), height(int)

    Returns: Returns none, Prints a number triangle based on the start, 
    step and height values entered.
    """
    # Store our num here which will be used to print out the numbers,
    # initial value is start...
    num = start
    # For each row in range from 1 to the height + 1...
    for row in range(1, height + 1):
        # Inner loop iterates to the length of the row..
        for i in range(row):
            # Prints the number right aligned with a space...
            print(f'{num:>3}', end=' ')
            # Num incremented by the step value.
            num += step
        # Print space a new line
        print()
    # Second loop prints the numbers descending from the height of the triangle...
    # For each row in range of height - 1, stopping at 0 and with a step value of -1...
    for row in range(height - 1, 0, -1):
        # Inner loop iterates the row...
        for i in range(row):
            # Print each value right aligned with a space...
            print(f'{num:>3}', end=' ')
            # Increment num by step value...
            num += step
        # Print a new line
        print()

numberTriangle(4, 4, 6)