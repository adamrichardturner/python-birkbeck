def readable(phoneNum):
    if len(phoneNum) != 10:
        print("Phone number must be 10 digit long")
    elif not phoneNum.isdecimal():
        print("Input must be all digits")
    else:
        return "(" + phoneNum[0:3] + ")" + phoneNum[3:6] + "-" + phoneNum[6:]

print(readable("4155551212")) # (415)555-1212
print(readable("5656391452")) # (565)639-1452
print(readable("5307343711")) # (530)734-3711
print(readable("41555451212")) # Phone number must be 10 digit long