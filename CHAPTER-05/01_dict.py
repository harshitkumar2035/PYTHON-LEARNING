# student = {
#     "name": "Harshit"
# }
# student["city"] = "Delhi"
# print(student)

#1 item delete karna
# student = {
#     "name": "Harshit",
#     "city": "Delhi",
# }

# del student["city"]
# print(student)


#2 length of dictionary
# student = {
#     "name": "Harshit",
#     "age": 21,
#     "city": "Delhi",
# }
# print(len(student))


# 3 different data types in dictionary
    
# student = {
#     "name": "Harshit",
#     "age": 21,
#     "height": 5.7,
#     "is_student": True
# }
# print(student)



# 4 dictionary with list as value
    
# student = {
#         "name": "Harshit",
#         "skills": ["Python", "HTML", "CSS", "ReactJS"]
#     }

# print(student["skills"])



# 5 dictionary ke ander dictionary

student = {
 "name": "Harshit",
"marks": {
    "Maths": 90,
    "Science": 85,
    "English": 95
    }
}

print(student["marks"]["Maths"])