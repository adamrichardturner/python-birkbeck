def sumOddSquares(start, stopInc):
    """
    Function that computes the sum of squares of the odd numbers
    between the start and stop, inclusive.
    E.G sumOddSquares(2, 100) will computes 3^2 + 5^2 + 7^2 + ... + 99^2

    Params: start (int), stop(int)

    Returns: A string containing the computations with a final total.
    E.G "3^2 + ... 99^2 = 166649".
    """
    # We will keep our total of the squared odd numbers here.
    total = 0
    # We will concatenate the mathematical expressions to this empty string.
    expressions = ""
    # If start > stopInc we complete the range in negative incremental steps.
    if start > stopInc:
        # We include both the start and stopInc numbers in the calculations as 
        # per the Markdown.
        for i in range(start, stopInc - 1, -1):
            # If iterator is an odd number (has remainders after dividing by 2)
            # We concatenate to the expressions string with the calculation ^2 +
            if i % 2 != 0:
                expressions += str(i) + "^2 + "
                # Here we square the odd number.
                total += i ** 2
    elif start < stopInc:
        # If the start is < stopInc we include both start / stopInc in the final
        # expressions and total.
        for i in range(start, stopInc + 1):
            if i % 2 != 0:
                expressions += str(i) + "^2 + "
                total += i ** 2
    else:
        print("Enter valid start and stop numbers...")
    # Here we print the expressions up to the final 3 chars, which include " + "    
    print(expressions[:-3] + " = " + str(total))

sumOddSquares(3, 99)