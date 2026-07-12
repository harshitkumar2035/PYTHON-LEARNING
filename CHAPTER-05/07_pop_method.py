# student = {
#     "name": "Harshit",
#     "age": 21,
#     "city": "Meerut"
# }

# removed_value = student.pop("age")

# print("Deleted Value :", removed_value)
# print(student)

# student = {
#     "name": "Harshit",
#     "age": 21
# }

# print(student.pop("name"))
# print(student)

# student = {
#     "name": "Harshit"
# }

# student.pop("city")

student = {
    "name": "Harshit"
}

print(student.pop("city", "Key Not Found"))