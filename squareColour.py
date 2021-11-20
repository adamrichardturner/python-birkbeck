def checkChessGrid():
    """
    Checks chess coordinate given as user input is valid.

    Params: None

    Returns: Coordinates after validation (List)
    """
    coordinate = input("Enter coord: ")
    # If coordinate is correct length...(2)
    if len(coordinate) == 2:
        a2h = "a" <= coordinate[0].lower() <= "h"
            # Checks whether coordinate is between a and h(incl) and 1 and 8(incl)
        one2eight = "1" <= coordinate[1] <= "8"
        if a2h and one2eight:
            # If a2h and one2eight are true, return the coordinates as a list..
            square = [coordinate[0].lower(), int(coordinate[1])]
            return square
    else:
        return None

def squareColour(square):
    """
    Checks whether coordinate given is on black or white
    
    Params: square(coordinates in list form)

    Returns: Whether the coordinate given is on a white or black
    square.
    """
    if len(square) == 2:
        # aceg stores boolean val for if square[0] is in the aceg coordinates...
        aceg = square[0] in "aceg"
        # even stores boolean val for if square[1] is even or not.
        even = square[1]%2 == 0
        # If the coordinate is not in aceg and even is true or in aceg and not even...
        if (not aceg and even) or (aceg and not even):
            # Return black
            return "black"
        else:
            # Else return white
            return "white"
    else:
        return None
    

def main():
    # squareInput takes the checkChessGrid coordinates...
    squareInput = checkChessGrid()
    # If squareInput is not None, call squareColour(squareInput)...
    if squareInput != None:
        squareColour(squareInput)
        # Print the result of whether the coordinate is black or white.
        print(squareInput, "is", squareColour(squareInput))
    else:
        print("Not valid coordinates..")

main()

# "A1" - ['a', 1] is black

# "b1" - ['b', 1] is white

# "h5" - ['h', 5] is white

# "u7" - Not valid coordinates..

# "9" - Not valid coordinates..