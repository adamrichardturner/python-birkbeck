def mean(*nums):
    """
    Returns the mean (average) value of the arguments.

    Params: nums(Tuple)

    Returns: Returns the mean value (Float)
    """
    # Validate whether nums is truthy, if so...
    if nums: 
        # Store our mean figure here...
        avg = 0
        # Loop through each num in the tuple...
        for num in nums:
            # Add to avg...
            avg += num
        # To avoid division by 0 error, return 0 if avg is 0...
        if avg == 0:
            return 0
        # Return avg / length of nums for the mean...
        return avg / len(nums)
    # Else, Error is printed...
    else:
        print("Enter at least one number.")

print(mean())
# prints "Enter at least one number."
# prints None
print(mean(0))
# prints 0.0
print(mean(1))
# prints 1.0
print(mean(3,4,5))
# prints 4.0