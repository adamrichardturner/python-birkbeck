# define the function
def fizzBuzz(num):
    """
    Takes a number as input, if number is divisible by 3
    it should return "Fizz". If divisibile by 5, it should
    return "Buzz". If divisible by 3 and 5 it should return
    "FizzBuzz". Otherwise it returns itself.

    Parameter: num (int)

    Returns: Strings "Fizz" if divisibile by 3, "Buzz" if
    divisible by 5 and "FizzBuzz" if divisibile by 3 & 5.
    """
    # If divisible by 15, returns FizzBuzz (3 * 5)
    if int(num) % 15 == 0:
        return "FizzBuzz"
    # If divisibile by 3, return "Fizz"    
    elif int(num) % 3 == 0:
        return "Fizz"
    # If divisibile by 5, return "Buzz"    
    elif int(num) % 5 == 0:
        return "Buzz"
    else:
    # If not divisible by any of these conditions, return
    # the original argument.
        return num

# call and print the results four times
# with arguments 30, 35, 36 and 26, respectively
print(fizzBuzz(30))
print(fizzBuzz(35))
print(fizzBuzz(36))
print(fizzBuzz(26))