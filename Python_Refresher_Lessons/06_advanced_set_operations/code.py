friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# local_friends = {"Rolf"} # hardcoded set, not helpful as it can't be modified
# find the difference between the two sets and return the non-common elements
local_friends = friends.difference(abroad)

# print(local_friends)
# set() is the notation of an empty set

# join sets
all_friends = local_friends.union(abroad)
# print(all_friends)

art_students = {"Bob", "Jen", "Rolf", "Charlie"}
science_students = {"Bob", "Jen", "Adam", "Anne"}

# those studying art but not science
# print(art_students.difference(science_students))
# those studying science but not art
# print(science_students.difference(art_students))
# those not studying art or science but not both
# print(art_students.difference(science_students).union(science_students.difference(art_students)))

# the students studying both art and science

##  Intersection
print(art_students.intersection(science_students))

# set1 = {14, 5, 9, 31, 12, 77, 67, 8}
# set2 = {5, 77, 9, 12}
# print(set1.intersection(set2)) # {5, 77, 9, 12}
