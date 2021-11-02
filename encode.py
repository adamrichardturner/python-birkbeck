def encode(myString, numBefore, numAfter):
    """
    Encrypts the message by specifying how to wrap each character. 
    
    E.G encode(myString, 2, 0) means to add two random chars before
    each character in myString, and none after.

    E.G encode(myString, 1, 3) means to add 1 random char before and
    3 randomm chars after each char in myString.

    Params: myString (a string to cipher), numBefore (number of random
    chars before each char in myString), numAfter (num of random chars 
    after each char in myString.)
    """
    # Import the required libraries to complete the random char generation.
    import random
    import string
    # We will store our random chars in before and after strings.
    randomBefore = ''
    randomAfter = ''
    # The final encoded string will be stored here.
    encoded = ''
    # For each number of chars to randomly generate before the myString
    # chars, concatenate these to the randomBefore string.
    for char in range(numBefore):
        randomBefore += random.choice(string.ascii_letters)
    # Same as above, except for number of chars to randomly generate after
    # myString chars.
    for char in range(numAfter):
        randomAfter += random.choice(string.ascii_letters)
    # Loop through each char in myString and concatenate with encoded each
    # char with the before and after random chars.
    for char in myString:
        encoded += randomBefore + char + randomAfter
    
    print(encoded)

encode("Help", 0, 0)
encode("Take the red", 2, 0)
encode("Meet at midnight", 3, 2)