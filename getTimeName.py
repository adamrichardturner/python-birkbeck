# Define the function
def getTimeName(hours, minutes):
    """
    Function that returns the English name for a point in time.
    E.G 5 o'clock, half past 3, a quarter past 11..

    Parameters: Hours (int), Mins (int)

    Returns: The time in spoken English as a string.
    """
    # If minutes == 1 return 1 minute past the hour in English.
    if minutes == 1:
        return "1 minute past " + str(hours)
    # If hour is 12 and minutes betweeen 30 and 45, return minutes to 1
    elif hours == 12 and 45 > minutes > 30:
        return str(60 - minutes) + " minutes to " + str(int(hours / hours))
    elif minutes == 0:
    # If minutes are 0, return the hour as o clock
        return str(hours) + " o'clock"
    elif minutes == 15:
        # if minutes == 15 return quarter past + hours
        return "a quarter past " + str(hours)    
    elif minutes == 30:
        # if minutes == 30 return half past + hours
        return "half past " + str(hours)
    elif 30 > minutes > 0:
        # if minutes less than 30 but greater than 0, use minutes past in the str
        return str(minutes) + " minutes past " + str(hours)
    elif minutes == 45 and hours == 12:
        # if minutes == 45 return quarter to + hours
        return "a quarter to " + "1"
    elif minutes == 59:
        # special case of 1 minute to the hour, 1 minute to the next hour
        return "1 minute to " + str(hours + 1)
    elif 60 > minutes > 30:
        # if < 60 mins and > 30 use "minutes to"
        return str(60 - minutes) + " minutes to " + str(hours + 1)

# Make 8 function calls to show it can correctly show all time points.
print(getTimeName(5,0))      # "5 o'clock"  
print(getTimeName(3,30))     # "half past 3"    
print(getTimeName(11,15))    # "a quarter past 11"  
print(getTimeName(12,1))     # "1 minute past 12"  
print(getTimeName(2,10))     # "10 minutes past 2"     
print(getTimeName(12,45))    # "a quarter to 1"   
print(getTimeName(3,59))     # "1 minute to 4"   
print(getTimeName(12,40))    # "20 minutes to 1"  