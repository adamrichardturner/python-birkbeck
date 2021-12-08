def median(*nums):
    """
    Median returns the median value of a list of numbers.
    
    Params: nums(Tuple)

    Returns: The median value (Float)
    """
    # Check if nums is a truthy value...
    if nums:
        # If the length of nums is even...
        if len(nums) % 2 == 0:
            # Find the upper middle and lower middle values, stored in a list after sorting nums
            # sum them...
            return sum([sorted(nums)[len(nums) // 2], sorted(nums)[len(nums) // 2 - 1]]) / 2
        else:
            # Else we just return the middle value (number at /2 index of nums)
            return nums[len(nums) // 2]
    else:
        print("Enter at least one number")

print(median(6, 3, 4, 1, 5)) # prints 4
print(median(6, 3, 4, 1, 5, 8)) # prints 4.5
print(median()) # prints "Enter at least one number" and None