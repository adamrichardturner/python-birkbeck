def readInteger():
    """
    Reads in a positive integer string from keyboard.
    If the input is not a digit then it prints error.
    If the integer string's last digit is 0 it prints error.
    If the integer string is valid it returns the string.
    Cycle continues until correct input.

    Params: None

    Returns: Error messages if string is not valid (String) or
    returns the string is valid (String).
    """
    # We store our flag here for valid input...
    valid = False
    # While the input is not valid yet...
    while not valid:
        # Take input...
        str = input("Please enter a positive integer: ")
        # If the input is not a digit, print error...
        if not str.isdigit():
            print("Input must be a positive integer")
        # Else if the input ends with a 0, print error...
        elif str[-1] == '0':
            print("Last digit must not be 0")
        # Else, break the loop by changing flag to True and return
        # the valid input...
        else:
            valid = True
            return str

# -1005, it prints "Input must be a positive integer"
# r, it prints "Input must be a positive integer"
# 1340, it prints "Last digit must not be 0"
# 1234567, it prints 1234567