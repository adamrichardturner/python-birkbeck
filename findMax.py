def findMax():
    """
    This function requires the user enter some floating point numbers
    from the keyboard. The user can press Enter to quit. It returns the
    largest of all the numbers. It should print out "The largest number is x"

    Params: None

    Returns: The largest number the user has entered.
    """
    # We will store our nums in this list.
    nums = []
    # While the length of the nums list is >= 0 our loop runs.
    while len(nums) >= 0:
        # We take user input and store it in variable called num.
        num = input("Enter a number (or press Enter to quit): ")
        # If num is empty (Enter) and no other numbers have been entered, we print
        # No number entered and break the loop.
        if num == "" and len(nums) == 0:
            print("No number entered")
            break
        # Else if num is empty (Enter) and there are numbers in the list, we 
        # print the largest number using the max function and break the loop.
        elif num == "" and len(nums) > 0:
            print("The largest number is " + str(max(nums)))
            break
        # If num has a truthy value we append the float of that number to the nums list.
        elif num:
            nums.append(float(num))

findMax()