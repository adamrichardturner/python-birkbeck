def allUpper(string):
    isUpperList = []
    for char in string:
        if char.isupper():
            isUpperList.append(char.isupper())
    return all(isUpperList)

def allUpper(string):
    return all("a" <= char <= "h" for char in string)

def allSymbols(string):
    isSymbolList = []
    for char in string:
        isSymbolList.append()