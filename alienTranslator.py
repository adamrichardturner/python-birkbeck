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

def alienSentence(sentence):
    """
    Function which takes in an English sentence without punctuation, turning it
    into the Alien Language following the rules for each word below: 
    
    - If the word begins with a consonant, it is moved to the end of the word and adds on 'ay'.
    - If the word begins with a vowel, way is just added to the end.
    - If the word begins with a symbol (non letter) the word is returned as the input was.
    - Returned words are displayed in lowercase. 
    - The sentence will start capitalized...

    Params: sentence(String)

    Returns: The sentence (String) converted to Alien Language as per the rules stated above in this 
    docstring.
    """
    sentences = sentence.split(" ")
    # Using list comprehension first, we run each word in sentences through the alienLatin(word) 
    # function, returning the list as a string using .join and with capitalize to make the first
    # letter uppercase...
    print(' '.join([alienLatin(word) for word in sentences]).capitalize())

def alienTranslator():
    """
    Takes user input after a welcome message and allows the user to enter sentences after each 
    carriage return, which are converted to the alien language and printed. If no input is entered 
    and enter is pressed, the program prints a Goodbye message and exits. Sentences are printed with a capital
    letter at the start and no punctuations are expected from the user.

    Params: None

    Returns: None - Instead, prints sentences converted to Alien Language following a Welcome Message
    and prints a Goodbye message if no input is entered. Markdown implies this as per the test cases:
    """
    # Print the welcome message...
    print("Welcome to the Alien Translator, please type sentences in English for extraterrestrial translation: ")
    # Our playing flag is a boolean value...
    playing = True
    # While playing is true...
    while playing:
        # Take user input...
        userSentence = input("Please enter a sentence to be converted to the Alien Language: ")
        # If the user has entered characters...
        if len(userSentence) > 0:
            # Call alienSentence with userSentence as the argument, it will print the translated sentence...
            alienSentence(userSentence)
        else:
            # Else if no input is entered, print the Goodbye message and change playing to False, thus
            # breaking the loop.
            print("No language to translate, exiting! Goodbye Human!")
            playing = False

alienTranslator()

"""
Test cases

[Your own greeting message here]

Enter i am a cat
Print Iway amway away atcay
Enter you are a star
Print Ouyay areway away tarsay
Enter This is Birkbeck
Print Histay isway irkbeckbay
Enter nothing

[Your own goodbye message]
"""
