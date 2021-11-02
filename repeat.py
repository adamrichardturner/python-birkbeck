# define the function
def repeat(string, n, delim):
    """
    Produces a string repeated n times, 
    separated by the delim. 

    Parameters: string(str), n(int), delim(str)

    Returns: The string repeated n times, separated
    by the delim.
    """
    # Return the string + delim n times, removing the
    # delim at the final instance of the repeated string.
    return ((string + delim) * n)[:-len(delim)]

# Call the function 3 times with the following:
print(repeat("jingle", 4, "&&"))
print(repeat("wow", 0, "*"))
print(repeat("kapow", 1, "%"))