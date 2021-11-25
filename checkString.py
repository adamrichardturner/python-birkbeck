def allUppercase(string):
    """
    Checks if all chars in a string are uppercase. 

    Params: string(string)

    Returns: True if the string contains all uppercase chars, false
    if not.
    """
    return all(char.isupper() for char in string)

def oneLetterLowercase(string):
    """
    Returns true if at least one letter is lowercase

    Params: string(string)

    Returns: True if any letter is lowercase 

    """
    return any(char.islower() for char in string)

def digitsOrUpper(string):
    """
    Checks if a string contains only digits or uppercase letters.

    Params: string(string)

    Returns: True if string contains only digits or uppercase letters.
    """
    return all(char.isupper() or char.isdigit() for char in string)

def allSymbols(string):
    """
    Checks if a string is made up all symbols only..

    Params: string(string)

    Returns: True if all symbols, false if not.
    """
    return all(not char.isalnum() for char in string)

def isCapitalEndPeriod(string):
    """
    Checks whether a string starts with a capital and ends with 
    a period.

    Params: string(String)

    Returns: True if string starts with capital and ends with .
    False if otherwise.
    """
    return string[0].isupper() and string[-1] == "."

print(allUppercase("TEST")) # True
print(allUppercase("TESt")) # False

print(oneLetterLowercase("TESt")) # True
print(oneLetterLowercase("TEST")) # False

print(digitsOrUpper("1234ASDV")) # True
print(digitsOrUpper("asd")) # False

print(allSymbols("*/#!")) # True
print(allSymbols("asd*/#!")) # False

print(isCapitalEndPeriod("Hello.")) # True
print(isCapitalEndPeriod("hello.")) # False