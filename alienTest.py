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

def alienTest():
    """
    Function that asks three questions with pre-determined answers (model answers). 
    
    If 2 or more questions are not solved, an alien message is printed to the user 
    "You are an alien" translated with an alien translator function. If this is not true, 
    "You are a human is printed". 

    Params: None

    Returns: None - Instead prints an output dependant on the answers as stipulated above.
    """
    # Store our model answers here in a list in order of questions to be asked in the inputs...
    models = [True, False, True]
    # Take user input and store in first, second and third variables..
    first = bool(input("Is 5 not greater than 6? "))
    second = bool(input("Is the different of 8 and 5 not smaller than or equal to the product of 1 and 3? "))
    third = bool(input("Is 2 raised to the power of 3 less than 3 raised to the power of 2? "))
    # Store our answers in a list...
    answers = [first, second, third]
    # Using list comprehension, we loop through both lists, comparing the values and store in solved a new list
    # which holds Boolean values as to whether the questions were answered correctly...
    solved = [i==j for i, j in zip(models, answers)]
    # Store our count here for False answers...
    count = 0
    # For each answer in solved...
    for answer in solved:
        # If the answer was false (Failed the question)...
        if answer == False:
            # Increment count..
            count += 1
    # If count >= 2 then..
    if count >= 2:
        # We call alienSentence translating "You are an alien" into Alien Language
        alienSentence("You are an alien")
    else:
        # Else we print you are a human...
        print("You are a human")

alienTest()
"""
Enter True, True and nothing and the message is (the alien translation of) You are an alien
Enter True, nothing and nothing and the message is You are a human
Enter nothing, True and nothing and the message is (the alien translation of) You are an alien
"""