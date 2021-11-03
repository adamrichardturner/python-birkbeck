def isPrime(num):
    """
    Takes an integer as an input and checks whether the num is a prime
    number, returning True or not if not prime (False). 

    A prime number is an integer that is greater than 1 and that has no
    positive divisors other than 1 and itself.

    Note: 1 is not a prime. 2, 3, 5, 7, 11, 13, 17, 19 are the prime numbers 
    less than 20.

    Params: Num (Integer) which we test for being prime or not.

    Returns: True if the number is prime, false if not.
    """
    # We will store our factors here and sanitise it at the end.
    factors = []
    # For each integer in the range inclusive of the stop number.
    for i in range(1, num + 1):
        # If the number has a factor (it is divisible evenly by that number)
        # we append it to factors.
        if num % i == 0:
            factors.append(i)
    # Now we sanitize factors. If there are exactly 2 factors, we have a prime
    # and return True. Else we do not, so we return False. 
    if len(factors) == 2:
        return True
    else:
        return False
    
print(isPrime(1)) # False
print(isPrime(2)) # True
print(isPrime(17)) # True
print(isPrime(91)) # False