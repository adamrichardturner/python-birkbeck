# define the function
def middle(str1):
    """
    Produces a string containing the middle character of str1 if 
    the length of str1 is odd, or the two middle characters if
    the length is even.  If the string is empty, return an empty
    string too.

    Parameters: str1(string) 

    Returns: String containing middle character if the length of
    the string is odd or the middle two characters if even. If
    the string is empty, return an empty string.
    """
    if isinstance(str1, str):
        if len(str1) == 0:
            return ""
        # If the input is a string, check if the length of it is
        # odd (has a remainder, is not 0)
        elif len(str1) % 2 > 0:
            # Return the char at index floor divided by 2. Returns
            # the middle character.
            return str1[len(str1) // 2]
        # If the input is even (has no remainder) return the char
        # at middle two indexes     
        else:
            return str1[len(str1) // 2 - 1] + str1[len(str1) // 2]
    else:
        return "Enter a valid input, must be a string."

# Run the function three times and print out the results with 
# "thankyou", "salmon" and ""
print(middle("thankyou"))
print(middle("salmon"))
print(middle(""))