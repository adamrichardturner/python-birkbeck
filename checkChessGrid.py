def checkChessGrid():
    coordinate = input("Enter coord")
    if len(coordinate) == 2:
        a2h = "a" <= coordinate[0] <= "h"
        one2eight = "1" <= coordinate[1] <= "8"
        if a2h and one2eight:
            square = [coordinate[0].lower(), int(coordinate[1])]
            return square
        else:
            return "Not a Chess Grid..."
    else:
        print("Please input string with 2 chars")