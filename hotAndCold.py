# Import random library for answer generation
import random
# Store our random answer between 1 and 100 here
answer = random.randint(1, 100)
# This is our flag which we change to True if the user wins in the loop.
win = False
# While not win (True) 
while not win:
    # Take user input and store as an integer in guess...
    guess = int(input("Enter a number between 1 and 100: "))
    # If the guess is less than answer, print COLD.
    if guess < answer:
        print("COLD")
    # Else if guess > answer, print HOT
    elif guess > answer:
        print("HOT")
    # Else the user selected the right answer and win becomes true, breaking
    # the loop.
    else:
        win = True
# If the user wins, this will be printed...
print("YOU WIN")


