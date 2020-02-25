# number = 7

# while True:
#     user_input = input("Would you would like to play? (Y/n) ")
#     if user_input == 'n':
#         break

#     user_number = int(input("Guess our number: "))
#     if(user_number == number):
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1: # the same as the elif above 
#         print("Close, you were off by one")
#     else:
#         print("Sorry you guessed wrong")

#     user_input = input("Would you would like to play again? (Y/n) ")

friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

# for grade in grades:
#     total += grade
# same as sum()
total = sum(grades)

print(f'Total: {total}')
print(f'Avg: {total / amount}')

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if (number % 2) == 0:
        evens.append(number)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ").lower()
if user_input == 'q':
    print("Quit")
elif user_input == "a":
    print("Add")