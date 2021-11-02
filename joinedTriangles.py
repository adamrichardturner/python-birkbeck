def joinedTriangles(side):
    """
    Draws up two joined-up isosceles right triangles.
    They share the tip (one asterisk)

    Params: side (integer) 

    Returns: Prints two joined isosceles triangles that share the
    tip (one asterisk).
    """
    # We iterate the range + 1 because we want to include the stop
    # number, as per the markdown joinedTriangles(8) prints 8 chars
    # on the first line.
    # The first loop prints descending from the side length.
    for i in range(side + 1):
        # If the iterator is the same as the side, we break the loop
        # to print out the last char as joined tip of the triangle.
        if i == side:
            break
        # In any other case, we print the side minus iterator, to produce
        # that iteration of the loop's string of asterisk.
        print((side - i) * '*')
    for i in range(2, side + 1):
        # We use 2 as our start of range to omit the 1st asterisk as that has
        # been printed by the above triangle already.
        # We print iterator * by asterisk to produce an ascending triangle.
        print(i * '*')

joinedTriangles(1)
joinedTriangles(5)
joinedTriangles(8)