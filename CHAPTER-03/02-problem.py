# Write a program to fill in a latter template given blow with name and date.
letter = ''' 
         Dear <|NAME|>,
         You are selected!
         Date: <|DATE|>
         '''
# 1st solution


# letter = '''
# Dear <|NAME|>,
# You are selected!
# Date: <|DATE|>
# '''

# name = input("Enter your name: ")
# date = input("Enter date: ")

# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>", date)

# print(letter)


#2nd solution

print(letter.replace("<|NAME|>", "Harshit").replace("<|DATE|>","30th may 2026"))