# Creating empty list to store our nums.
nums = []
# For each item in range of the numbers to input (user to input 5 numbers)
for i in range(5):
    # Take user input as int
    num = int(input("Please enter a number: "))
    # Append the number to the list as integer
    nums.append(num)
# Ask user if they want to keep the number they entered?
keep = input("Do you want to keep the last number you entered? Y / N ").upper()
# Markdown suggests to print the numbers before removing the smallest in in the remaining list.
print("The numbers you entered were: ", nums)
if keep == "N":
    # If the user does not want to keep the last number, we use pop() to remove it.
    nums.pop()
# Store the minimum num in this variable.
minimum = min(nums)
# While minimum is still in nums...
while minimum in nums:
    # Remove minimum.
    nums.remove(minimum)
# Printing the numbers after removing minimum value completely.
print("After removing the smallest number in every instance your numbers are: ", nums)