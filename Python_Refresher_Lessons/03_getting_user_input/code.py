# name = input('What is your name?') # Asks at the terminal prompt for the users input
# print(f"Hi there {name}")

# Converting string to a number
size_input = input("How big is your house (in square feet)?")
square_feet = int(size_input) # Converts to a integer
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} square meters")

# the :.2f rounds a floating point to 2 decimal places