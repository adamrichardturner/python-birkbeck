def checkChessGrid():
    """
    Checks chess coordinate given as user input is valid.

    Params: None

    Returns: Coordinates after validation (List)
    """
    coordinate = input("Enter coord")
    if len(coordinate) == 2:
    # If coordinate is correct length...(2)
        a2h = "a" <= coordinate[0] <= "h"
        # Checks whether coordinate is between a and h(incl) and 1 and 8(incl)
        one2eight = "1" <= coordinate[1] <= "8"
        if a2h and one2eight:
            # If a2h and one2eight are true, return the coordinates as a list..
            square = [coordinate[0].lower(), int(coordinate[1])]
            return square
        else:
            # Otherwise, return error...
            return "Not a Chess Grid Coordinate..."
    else:
        return "Please input coordinate with 2 chars"