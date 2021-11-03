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

    Returns: A string encoded with random chars before and after each
    char as per user input of the number of random chars before and after
    each char in myString.
    """
    # Import the required libraries to complete the random char generation.
    import random
    import string
    # The final encoded string will be stored here.
    encoded = ''
    # Loop through each char in myString and concatenate with encoded each
    # char with the before and after random chars.
    for char in myString:
        # For each iteration of each char, generate random chars dependant on the numBefore
        # and numAfter range. The variables will be re-assigned on each iteration, generating
        # completely random chars.
        randomBefore = ''.join(random.choice(string.ascii_letters) for i in range(numBefore))
        randomAfter = ''.join(random.choice(string.ascii_letters) for i in range(numAfter))
        encoded += randomBefore + char + randomAfter
    
    print(encoded)

encode("Help", 0, 0)
encode("Take the red", 2, 0)
encode("Meet at midnight", 3, 2)