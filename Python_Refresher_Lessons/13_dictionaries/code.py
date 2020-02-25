# key values pairs

friend_ages = { "Rolf": 24, "Adam": 30, "Anne": 27 }

# access via key 
friend_ages["Adam"] # 30

# add to a dictionary
friend_ages["Bob"] = 20

# Edit a dictionary value
friend_ages["Bob"] = 21
print(friend_ages)

friends = [
  {
    "name": "Rolf",
    "age": 30
  }, {
    "name": "Adam",
    "age": 29
  }, {
    "name": "Anne",
    "age": 28
  },
]

print(friends)
print(friends[1]["name"])

student_attendance = {
    "Rolf": 96, "Bob": 80
}

# for student in student_attendance:
#   print(f"{student}: {student_attendance[student]}")

print(student_attendance.items())
# .items() returns the dictionary pairs .e.g. [('Rolf', 96), ('Bob', 80)]
# then for index 0, student becomes 'Rolf' and attendance becomes 96
# (destructured) 
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print(f"z Bob: {student_attendance['Bob']}")
else: 
    print("Bob is not a student in this class")

attendance_values = student_attendance.values()
print("Class average: ", sum(attendance_values) / len(attendance_values))

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")
