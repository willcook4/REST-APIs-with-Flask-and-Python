# List a modifiable collection
# Always keeps the order
l = ["Bob", "Anne", "Rolf"]

# Tuple, can't be modified
# Always keeps the order
t = ("Bob", "Anne", "Rolf")

# Set, can be modified but cant have duplicate values
# order is not guarenteed, so cant use subscript notation to get items or use methods like .append
# 
s = {"Bob", "Anne", "Rolf"}

# Subscript notation item[0]
# e.g. l[1] = "Anne"

# Replacing/modifying list items
l[2] = "Sam"
print(l) # ["Bob", "Anne", "Sam"] 

# Add an item to a list
l.append("Fran")

# Remove an item from a list
l.remove("Bob")
print(l)

# Adding to a Set
s.add("Troy")
print(s)