# define the celsius to fahrenheit function
def celsius_to_fahrenheit(temp):
        """
        Converts celsius to fahrenheit

        Parameters: temp (int, float)

        Returns: Celsius converted to fahrenheit
        """
        return (temp * 9/5) + 32

# call the function twice and print out the results
# use 0 and 100 as arguments, respectively

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))