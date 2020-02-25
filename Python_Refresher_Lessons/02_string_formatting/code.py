name = 'Bob'
greeting = f"Hello, {name}" # f-sting, preferred!!

print(greeting)


name = 'Tom'
say_hi = "Hello, {}" # template string 
# .format()
with_name = say_hi.format(name) # name gets put in place of the curly brackets
print(with_name)

# multiple args as a template string
longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Jeff", "Monday")
print(formatted)

