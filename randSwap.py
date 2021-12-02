import random

def randSwap(word):
    """
    Swaps two random characters in a string

    Params: word(string)

    Returns: The same string but with two characters swapped
    in position randomly.
    """
    # We store our length of word here...
    length = len(word)
    if length < 2:
        return "String length should be at least 2."
    else:
        # i and j stores a random position in the string
        i = random.randint(0, length - 2)
        j = random.randint(i + 1, length - 1)
        # first stores the word up to not including i...
        first = word[:i]
        # mid stores the word from 1 after i upto and not including j
        mid = word[i+1:j]
        # last stores the word from j+1 upto the end...
        last = word[j+1:]
        # Return the word with the two characters randomly swapped...
        return first + word[j] + mid + word[i] + last

print(randSwap(""))
print(randSwap("s"))
print(randSwap("st"))
print(randSwap("string"))