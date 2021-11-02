# define the celsiusToFahrenheit function
def celsiusFahrenheit(temp, unit):
    """
    This function takes in a temperature in celsius
    or fahrenheit and a unit to define the conversion.
    If C is entered (for celsius) it converts to fahrenheit.
    If F is entered (for fahrenheit) it converts to celsius.

    Parameters: temp (int, float), unit (str)
    
    Returns: Temp converted from Celsius to Fahrenheit or 
    Fahrenheit to Celsius, depending on the unit used.
    """
    # If the input is in any case C, convert to
    # fahrenheit.
    if unit.upper() == "C":
        # Round the result to two decimal places 
        # and return it.
        return round((temp * 9/5) + 32, 2)
    elif unit.upper() == "F":
        # If input is F in any case, convert to
        # celsius.
        return round((temp - 32) * 5 / 9, 2)
    else:
        # If the input is something else, print error
        # and return None.
        print("Please enter a valid input")
        return None

# Call the function three times and print out the results.
print(celsiusFahrenheit(10, "C"))
print(celsiusFahrenheit(52, "f"))
print(celsiusFahrenheit(10, "e"))