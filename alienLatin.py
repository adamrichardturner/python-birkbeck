def alienLatin():
    """
    Asks user for input in word (String) form and returns an alien language
    version of the input. 
    
    - If the word begins with a consonant, it is moved to the end of the word and adds on 'ay'.
    - If the word begins with a vowel, way is just added to the end.
    - If the word begins with a symbol (non letter) the word is returned as the input was.
    - Returned words are displayed in lowercase. 

    Params: None

    Returns: The user input as a string as per the above rules listed in bullet point form.
    """
    # Store our user input here...
    word = input("Please enter your word to be converted to Alien Latin: ")
    # We will test against vowels, as all non-vowels are consonants...
    vowels = ["a", "e", "i", "o", "u"]
    # If the first char in the word is not in the alphabet...
    if not word[0].isalpha():
        # Return the word...
        return word
    # Else if the word's first charis in vowels....
    elif word[0].lower() in vowels:
        # Return the word in lowercase with way appended to the end...
        return word.lower() + "way"
    # Otherwise, we have start with a consonant. Return the word minus the 1st char
    # + the char in lowercase + "ay"
    else:
        return word[1:].lower() + word[0].lower() + "ay"

print(alienLatin())
"""
Enter pig, returns igpay
Enter banana, returns ananabay
Enter order, returns orderway
Enter Inspire, returns inspireway
Enter PEACH, returns eachpay
Enter ?Really!, returns ?Really!
Enter 76ers, returns 76ers
"""