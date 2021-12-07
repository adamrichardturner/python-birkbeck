def main():
    def readInteger():
        """
        Reads in a positive integer string from keyboard.
        If the input is not a digit then it prints error.
        If the integer string's last digit is 0 it prints error.
        If the integer string is valid it returns the string.
        Cycle continues until correct input.

        Params: None

        Returns: Error messages if string is not valid (String) or
        returns the string is valid (String).
        """
        # We store our flag here for valid input...
        valid = False
        # While the input is not valid yet...
        while not valid:
            # Take input...
            str = input("Please enter a positive integer: ")
            # If the input is not a digit, print error...
            if not str.isdigit():
                print("Input must be a positive integer")
            # Else if the input ends with a 0, print error...
            elif str[-1] == '0':
                print("Last digit must not be 0")
            # Else, break the loop by changing flag to True and return
            # the valid input...
            else:
                valid = True
                return str

    def addComma(string):
        """
        Adds a comma at every 3 characters of a string.

        Params: string (String)

        Returns: A string with commas at every third position.
        """
        # Using string slicing + join, we loop through the string and add comma at 3rd interval in steps of 3...
        return ','.join([string[i:i+3] for i in range(0, len(string), 3)])
    
    # Store our integer here...
    num = readInteger()
    # As per markdown, print the reverse of the number with commas added at third intervals...
    print(addComma(num)[::-1])

main()