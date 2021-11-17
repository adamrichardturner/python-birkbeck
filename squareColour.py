def checkChessGrid():
    coordinate = input("Enter coordinate!")
    if len(coordinate) == 2:
        a2h = "a" <= coordinate[0] <= "h"
        one2eight = "1" <= coordinate[1] <= "8"
        if a2h and one2eight:
            square = [coordinate[0].lower(), int(coordinate[1])]
            return square
        else:
            return "Erorr message 1"
    else:
        print("Please input string with 2 chars")

def squareColour(square):
    aceg = square[0] in "aceg"
    even = square[1]%2 == 0

    if (not aceg and even) or (aceg and not even):
        return "black"
    else:
        return "white"

def main():
    squareInput = checkChessGrid()
    if squareInput != None:
        squareColour(squareInput)
        print(squareInput, "is", squareColour(squareInput))

main()