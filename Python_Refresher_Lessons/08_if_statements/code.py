# string.lower() turns a string into lowercase

day_of_week = input("What day of the week is it today?").lower()

# if day_of_week = "Monday"
# print(day_of_week == "Monday")

if day_of_week == "monday":
    # this runs
    print('Have a great start to your week')
elif day_of_week == "tuesday":
    print("Getting there")
else:
    print("Full steam")

print("This always runs")