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

def centralNumber(type, *nums):
    """
    Takes two inputs, type (mean, median or mode) and nums
    a variable length tuple of numbers.

    Params: type(String), nums(Tuple)

    Returns: Either the mean, median or mode (as a number) of the nums entered, 
    dependant on the type entered by the user.
    """
    # Check if nums is truthy...
    if nums:
        # If type is mean, median, or mode - we call the respective functions and return them...
        if type == "mean":
            return mean(*nums)
        elif type == "median":
            return median(*nums)
        elif type == "mode":
            return mode(*nums)
        # Else we print an error...
        else:
            print("Incorrect type.")
    # Else we print an error...
    else:
        print("Enter at least one number.")

print(centralNumber("mode", 1))
print(centralNumber("mean", 1))
print(centralNumber("median", 1))
print(centralNumber("mode", 3, 3, 3, 4, 5))