def mode(*nums):
    """
    Returns the number that appears mostly frequently (mode) in a tuple.

    Params: nums(Tuple - variable length)

    Returns: The mode value, number that appears most often.
    """
    # First we check if nums is truthy...
    if nums:
        # If so, we return the maximum value with a key of count (how many times it appears)
        return max(nums, key=nums.count)
    else:
        # Else we print an error...
        print("Enter at least one number")

print(mode(6, 3, 9, 6, 6, 5, 9, 3)) # prints 6
print(mode(3, 3, 3, 4, 4, 4, 5)) # prints 3
print(mode()) # prints "Enter at least one number" and None