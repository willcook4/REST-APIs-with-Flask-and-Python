numbers = [1, 3, 5]

# list comprehension is lists from other lists
doubled = [x * 2 for x in numbers]
# variable doubled equals a list of the numbers in the list multiplied by 2 for each number in numbers 

# traditionally done in a for loop, now done with list comprehension
# for num in numbers:
#   doubled.append(num * 2)

friends = ["Rolf", "Sam", "Simon", "Sarah", "Jen"]
starts_s = []

# for friend in friends:
#   if(friend.startswith("S")):
#     starts_s.append(friend)

# replaced with the list comprehension
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)