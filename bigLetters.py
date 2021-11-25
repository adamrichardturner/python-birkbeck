def stars(n):
    """
    Produces asterisk on one line of n length.

    Params: n (int)

    Returns: Asterisk line of n length.
    """
    return "*" * n + "\n"

def splitStars(starList):
    """
    Produces asterisk line based on a list input.

    Params: starList(list)

    Returns: Asterisk lines where 1 is in the list and space 
    where any other member is in the list.
    """
    # We store our final string representation here...
    starStr = ""
    # For each member of starList...
    for n in starList:
        # If n is a 1, print a *
        if n == 1:
            starStr += "*"
        else:
            # Else if not 1, print a space...
            starStr += " "
    return starStr + "\n"

LETTER_H = splitStars([1,0,0,0,1]) * 2 + stars(5) + splitStars([1,0,0,0,1]) * 2
LETTER_E = stars(5) + stars(1) + stars(4) + stars(1) + stars(5)
LETTER_L = stars(1) * 2 + stars(1) + stars(5)
LETTER_O = splitStars([0,1,1,1,0]) + splitStars([1,0,0,0,1]) * 3 + splitStars([0,1,1,1,0])
print(LETTER_H + LETTER_E + LETTER_L + LETTER_L + LETTER_O)