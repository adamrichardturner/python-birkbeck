def discount(*purchases):
    """
    Takes a tuple of purchase prices. If at least 5 items are purchased
    and the total price is at least £60 a 20% discount is applied. 
    Prints a success message and total value after discount if above conditions 
    are met. Otherwise, prints just the total value of purchases.

    Params: Purchases(Tuple)

    Returns: Total value (Number) after discount if at least 5 items purchased &
    total value is £60 or more before discount. Otherwise just returns the sum of
    the purchases value.
    """
    # First we check if the input is a tuple...
    if isinstance(purchases, tuple):
        # If the length of the tuple is >=5 and purchase value total is above £60...
        if len(purchases) >= 5 and sum(purchases) >= 60:
            # Print success message and apply discount...
            print("Congrats! Discount applies!")
            return sum(purchases) * 0.8
        # Else, we print a message stating no discount and the sum of the purchases
        # without discount applied.
        else:
            print("Sorry, no discount")
            return sum(purchases)

print(discount(56, 35)) #91
print(discount(5, 6, 2, 4, 7)) #24
print(discount(12, 12, 12, 12, 12)) #48.0
print(discount(12, 12, 12, 12, 11)) #59
print(discount(60)) #60
print(discount(0)) #0