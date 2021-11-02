# define the function
def speedometer(speed, limit):
    """
    If speed is less than or equal to the speed limit, it should print “Ok”.
    Otherwise, for every 5km above the speed limit, it should give the driver one 
    demerit point and print the total number of demerit points.

    If the speed is 80 and the speed limit is 70, it should print: “Points: 2”.

    If the speed is 84 and the speed limit is 70, it should print: “Points: 2”.

    If the driver gets more than 12 points, the function should print: “License suspended”

    Parameters: speed(int), limit(int)

    Returns: As above various demerits, warning and "OK" if the speed is below the 
    limit.
    """
    # Counts how many times above the limit the driver goes.
    count = 0
    # If speed below or equal to the limit, prints OK
    if speed <= limit:
        print("Ok")
    # Else if the speed > limit iterate through the range of nums
    # including limit upto speed. 
    elif speed > limit:
        for i in range(limit, speed):
            # Increment the count variable by 1 on each iteration. This gives us the total
            # number above the limit the driver was.
            count += 1
        if count / 5 > 12: 
            # If the count divided by 5 (num of points) is greater than 12, return license
            # suspended.
            return "License suspended"
        else:
            # Otherwise, return the points incurred. 
            return "Points: ", int(count / 5)
    
# call the function 5 times with these test cases:
print(speedometer(220, 100))
print(speedometer(115, 110))
print(speedometer(129, 90))
print(speedometer(85, 90))
print(speedometer(94, 90))