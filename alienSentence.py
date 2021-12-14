def alienLatin(word):
    """
    Takes in a word (String) and returns that word converted into an Alien Language as per the 
    rules stated below:
    
    - If the word begins with a consonant, it is moved to the end of the word and adds on 'ay'.
    - If the word begins with a vowel, way is just added to the end.
    - If the word begins with a symbol (non letter) the word is returned as the input was.
    - Returned words are displayed in lowercase. 

    Params: word(Singular Word in String Form)

    Returns: The word as a string as per the above rules listed in bullet point form.
    """
    # Store our user input here...
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

def alienSentence():
    """
    Function which takes in an English sentence without punctuation, turning it
    into the Alien Language following the rules for each word below: 
    
    - If the word begins with a consonant, it is moved to the end of the word and adds on 'ay'.
    - If the word begins with a vowel, way is just added to the end.
    - If the word begins with a symbol (non letter) the word is returned as the input was.
    - Returned words are displayed in lowercase. 
    - The sentence will start capitalized...

    Params: None (Markdown implies user input is taken at the keyboard)

    Returns: The sentence converted to Alien Language as per the rules stated above in this 
    docstring.
    """
    # Store our user input sentence here, expecting no punctuation as per markdown...
    sentence = input("Please enter a sentence to be translated to Alien Latin: ")
    # Split the sentence into words within a list...
    sentences = sentence.split(" ")
    # Using list comprehension first, we run each word in sentences through the alienLatin(word) 
    # function, returning the list as a string using .join and with capitalize to make the first
    # letter uppercase...
    return ' '.join([alienLatin(word) for word in sentences]).capitalize()

print(alienSentence())
# Enter how are you, returns Owhay areway ouyay '
# Enter My name is Oliver, returns Ymay amenay isway oliverway
# Enter there are 24 hours in a day, returns Heretay areway 24 ourshay inway away ayday
