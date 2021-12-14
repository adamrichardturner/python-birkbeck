def isLeap(year):
    """
    Determines if the year is a leap year or not.
    """
    import calendar
    return calendar.isleap(year)

def validateDate(dd=31, mm=1, yyyy=1900):
    """
    Validates a date is in the correct form. 
    Day: Between 1 - 31
    Month: Between 1 - 12
    Year: Between 0 - 9999

    Params: dd, mm, yyyy (All Integers)

    Returns: True or False (Boolean), True if the date is valid
    or False if not.
    """
    # First validate the year and month is in correct format...
    if 0 <= yyyy <= 9999 and 1 <= mm <= 12:
        # If mm is a month with less than 31 days...
        if (mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11):
            # Check if Feb and it is a leap year, validate the days...
            if mm == 2 and isLeap(yyyy) and 1 <= dd <= 29:
                return True
            # Else if not a leap year and days are correct...
            elif mm == 2 and not isLeap(yyyy) and 1 <= dd <= 28:
                return True
            # Else if a day with less than 31 days but not Feb, validate days...
            elif mm != 2 and 1 <= dd <= 30:
                return True
            else:
                return False
        else:
            # For all other months....validate days...
            if 1 <= dd <= 31:
                return True
            else:
                return False
    else:
        return False
        

print(validateDate()) # True
print(validateDate(31, 4, 1999)) # False
print(validateDate(29, 2, 1900)) # False
print(validateDate(29, 2, 2020)) # True
print(validateDate(mm=6)) # False
print(validateDate(mm=6, dd=0)) # False
print(validateDate(yyyy=10001)) # False