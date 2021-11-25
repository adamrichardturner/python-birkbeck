def isPalindrome(content):
    """
    Takes an input and confirms whether it is an alphanumeric palindrome or not.

    Params: content(Any)

    Returns: True if the input is a alphanumeric palindrome, false if otherwise.
    """
    # Convert our input into a string in lowercase
    content = str(content).lower()
    # We will validate our content here...
    valid = ""
    # For each char in content...
    for char in content:
        # If the char is alphanumeric...
        if char.isalnum():
            # Concatenate with valid...
            valid += char
    # If valid is the same as valid reversed...
    if valid[:] == valid[::-1]:
        # Return True
        return True
    else:
        # Else return False
        return False

print(isPalindrome(121)) # True
print(isPalindrome("deed")) # True
print(isPalindrome("Rotor")) # True
print(isPalindrome("Madam, I'm Adam.")) # True
print(isPalindrome("friend")) # False
print(isPalindrome(1234))# False