def countNegatives():
    """
    Function that counts and reports how many values are negative
    in a sequence of integers entered by the user. Press 'Enter' 
    to quit.

    Params: None

    Returns: Prints a string stating how many negative numbers. If 
    there is more than one negative number a plural will be used for
    'numbers'. 
    """
    # We will store our count of negative numbers in the sequence here.
    count = 0
    # While count is greater than or equal to 0 the loop will run, unless
    # the user presses only the enter key, in which case we print the count
    # of negative numbers and end the loop.
    while count >= 0:
        # We keep our input in this num variable as a string as we want to 
        # test for Enter key input too, and convert to int where required.
        num = input("Enter a number: ")
        if num == "" and count == 1:
        # If the user exits (blank input) and count is 1 we return singular
        # negative number and break the loop.
            print("There is " + str(count) + " negative number.")
            break
        # If the input is empty and count is 0, it will return 0 negative numbers.
        elif num == "" and count == 0:
            print("There are " + str(count) + " negative numbers.")
            break
        # If the input is Enter only and count above 0, we print the plural including
        # count of negative nuumbers.
        elif num == "" and count > 0:
            print("There are " + str(count) + " negative numbers.")
            break
        # If the input is a negative number, increment count.
        elif int(num) < 0:
            count += 1

countNegatives()