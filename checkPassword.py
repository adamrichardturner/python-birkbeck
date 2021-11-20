# We will store our password here...
password = "123456"
# For each item in range 1 -- 3(inclusive)
for i in range(1, 4):
    # Store userPass here
    userPass = input("Please enter your password: ")
    # If it is the third turn and password still incorrect...
    if i == 3 and userPass != password:
        # Print locked out message...
        print("Too many attempts. Account locked.")
        break
    # Else if userPass = password we have a match and print the success message
    # and break the loop...
    elif userPass == password:
        print("Password correct! Welcome!")
        break
    # Else if password incorrect state invalid input...
    else:
        print("Invalid input")

#123456 # "Password correct! Welcome!"
#12, 123456 # "Invalid input", "Password correct! Welcome!"
#12, 1234, 123456 # "Invalid input", "Invalid input", "Password correct! Welcome!"
#12, 123, 1234 # "Invalid input", "Invalid input", "Invalid input", "Too many attempts. Account locked."