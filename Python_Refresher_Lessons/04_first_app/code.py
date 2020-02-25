user_age = int(input("Enter your age: ")) # convert to an integer
# years = int(user_age) 
months = user_age * 12
# 1 common year = 365 days = (365 days) × (24 hours/day) × (3600 seconds/hour) = 31536000 seconds
seconds = 365*24*3600*user_age
print(f"Your age in {user_age}, is equal to {months} months or {seconds} seconds")
