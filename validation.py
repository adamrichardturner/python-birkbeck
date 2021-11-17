def main():
    """
    Prints out a list based on whether its first char is between A <= H and
    second char is a digit between 1 and 8 inclusive.

    Params: None

    Returns: A list if passes validation, errors if not.
    """
    # We will store our string here...
    str = input("Please type two characters and press enter: ")
    # If the str length isn't two as specified...
    if len(str) != 2:
        # Error!
        print("Error: Must be two characters.")
    # Elif, str[0] between a and h incl, and 1 and 8 incl...
    elif "a" < str[0].lower() <= "h" and "1" < str[1] <= "8":
        # Save the string as a list, as per markdown...
        strList = [str[0].lower(), int(str[1])]
        # Print list...
        print(strList)
    else:
        # Else error!
        print("Does not meet requirement.")

main()

# "A10" = Error: Must be two characters.
# "Z9" = Does not meet requirement.
# "B4" = ['b', 4]
# "G3" = ['g', 3]
# "a0" = Does not meet requirement.
# "c8" = ['c', 8]