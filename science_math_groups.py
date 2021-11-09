# Create lists sciA and sciB
sciA = ['E', 'D', 'A', 'C', 'B']
sciB = ['I', 'F', 'J', 'H', 'G']

# Merge sciA and sciB into sciA - used shorthand operator for this.
sciA += sciB

# Dismiss the group sciB. Deleting group.
del sciB


# Sort sciA from the smallest to the greatest. Use sort()
sciA.sort()


# 'H' left the group and 'K' filled in the position. 
# You should not directly use the index of 'H'. 
sciA.insert(sciA.index("H"), "K")
sciA.remove("H")
# The last member in sciA left 
sciA.pop()


#'L' and 'M' joined
sciA.append("L")
sciA.append("M")

# Report how many kids are in the 
# group now by calling a function
print(len(sciA))

# Print the name at 5th position (the first is 'A')
print(sciA[4])


# Same group of kids formed the math group mathGroup.
mathGroup = list(sciA)


# The math group's third member (the first is 'A') left
# 'P' took the place. Use one statement for this
mathGroup[2] = "P"


# Print out the math group and science group.
print(mathGroup)
print(sciA)


# Enumerate the math group members starting from 1
for i, student in enumerate(mathGroup, start=1):
    print(i, student)

# Enumerate the science group members starting in the sequel of the math group
# For instance, math group's last is (15, ..), then the science group's first will be (16, ..)
for i, student in enumerate(sciA, start=len(mathGroup) + 1):
    print(i, student)

