def time2Midnight(time):
    """
    Displays the time to midnight when given a string containing the current
    time in the format hh:mm:ss

    Params: time(string) in the form hh:mm:ss 

    Returns: Time to midnight in string format as hh:mm:ss form.
    """
    # We store our hh, mm, ss in these variables...
    hh, mm, ss = time.split(":")
    hours = int(hh)
    mins = int(mm)
    secs = int(ss)
    # If hours, mins and secs are 0...
    if hours == 0 and mins == 0 and secs == 0:
        # Return 0 time until midnight in hh:mm:ss form...
        return '0:0:0'
    # Else if mins and secs are 0 return 24 - hours in the hours slot + 0s...
    elif mins == 0 and secs == 0:
        return str(24 - hours) + ":0:0"
    else:
        # Else we have digits in hours, mins and secs...
        # Hours is = 23 minus hours...
        h = str(23 - hours)
        # If secs are 0...
        if secs == 0:
            # Return hours + : + 60 - mins + 0
            return h + ":" + str(60 - mins) + ":0"
        else:
            # Secs are not 0, return hours + 59 - mins, + 60 - secs
            return h + ":" + str(59 - mins) + ":" + str(60 - secs)

print(time2Midnight("00:00:00")) # prints 0:0:0
print(time2Midnight("10:00:00")) # prints 14:0:0
print(time2Midnight("10:30:00")) # prints 13:30:0
print(time2Midnight("13:34:59")) # prints 10:25:1