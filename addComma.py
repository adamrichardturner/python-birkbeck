def addComma(string):
    """
    Adds a comma at every 3 characters of a string.

    Params: string (String)

    Returns: A string with commas at every third position.
    """
    # Using string slicing + join, we loop through the string and add comma at 3rd interval in steps of 3...
    return ','.join([string[i:i+3] for i in range(0, len(string), 3)])

print(addComma("458")) # returns and prints"458"
print(addComma("45876")) # returns and prints"458,76"
print(addComma("458763")) # returns and prints"458,763"
print(addComma("4587632")) # returns and prints "458,763,2"