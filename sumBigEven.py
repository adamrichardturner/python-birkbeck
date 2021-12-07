def sumBigEven(nList):
    """
    Takes a list of integers as input and sums all even 
    numbers that are greater than 10. If the input is empty
    it returns -1

    Params: nList (List)

    Returns: The sum of all even numbers greater than 10 (Int)
    or returns -1 if input is empty.
    """
    # If the nList is not Truthy (has no values) return -1
    if not nList:
        return -1
    # Else...
    else:
        # We store our final sum here...
        sum = 0
        # For each num in nList..
        for num in nList:
            # If the num > 10 and it is even...
            if num > 10 and num % 2 == 0:
                # Add to our sum variable...
                sum += num
        # And finally return the sum.
        return sum
    
print(sumBigEven([])) # prints -1
print(sumBigEven([1, 2])) # prints 0
print(sumBigEven([13, 16, 10, 4, 6, 17, 9, 20])) # prints 36