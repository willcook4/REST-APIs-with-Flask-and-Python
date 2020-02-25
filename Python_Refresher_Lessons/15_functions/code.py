def hello():
    print("Hello!")

hello() # call the function


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds: {age_seconds}")


print("Welcome to the program!")
user_age_in_seconds()
print("Goodbye")

# Note functions are not hoisted like in JavaScript,
# you must define them before you call them

def add(x, y): # x and y are parameters
  result = x + y
  print(result)

add(5, 3) # 5 and 3 are arguments

# hello("Bob") # will error as there are no parameters required 

# add() # Must provide arguments to match the parameteres. 
# Will error with: TypeError: add() missing 2 required positional arguments: 'x' and 'y'



def say_hello(name, surname):
  print(f"Hello, {name} {surname}")
# named arguments or keyword arguments
say_hello(surname="Tom", name="Jones") 

# default parameter values

def subtract(x, y=2):
  print(x - y)

subtract(8, 3) # prints 5, 8 - 3 
subtract(8) # prints 6, 8 - default value of 2