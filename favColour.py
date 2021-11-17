def favColour(colour):
    """
    Returns true if given input is matched as a favourite colour.

    Params: colour(String)

    Returns: True if colour is in primaryColours chosen or False otherwise.
    """
    # We will store our primary colours in this list...
    primaryColours = ["red", "green", "blue"]
    # If the colour passed in as arg is in the above list...
    if colour in primaryColours:
        # Return true
        return True
    else:
        # Else return false
        return False

def main():
    # We store the user input of their colour in variable colour as lowercase
    colour = input("Enter your favourite colour: ").lower()
    # If that colour, passed in to the favColour func...
    if favColour(colour):
        # Return this if true...
        print("I like " + colour + " too")
    else:
        # Else return this...
        print(colour.capitalize() + " is not my favourite colour")

main() # rED = I like red too
main() # yeLLow = Yellow is not my favourite colour
main() # GREEN = I like green too
main() # blue = I like blue too
