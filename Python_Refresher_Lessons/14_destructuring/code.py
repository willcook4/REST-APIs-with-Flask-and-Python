# x = (5, 11)
# same as
x = 5, 11

x, y = 5, 11 # shorthand for x=5, y=11

t = 23, 14
s, g = t

print(s, g)

student_attendance = {
  "Rolf": 96, "Bob": 80, "Anne": 100
}

print("list: ", list(student_attendance.items()))

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")


# use _ to mark values as nuot needed
person = ("Bob", 42, "Mechanic")
name, _, profession = person # using _ to ignore the variable we dont want to destuctre
print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head) # 1
print(tail) # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]
print(head) # [1, 2, 3, 4]
print(tail) # 5

head, tailbone, *tail = [1, 2, 3, 4, 5]
print(head) # 1
print(tailbone) # 2
print(tail) # [3, 4, 5]
