# Arithmetic Operators
a = 10
b = 5
c = a + b  # Addition
print(c)  # Output: 15     


# Assignment Operators
x = 10
x += 5  # Equivalent to x = x + 5   
print(x)  # Output: 15


# Comparison Operators
p = 10
q = 20
print(p > q)  # Output: False
print(p < q)  # Output: True
print(p == q) # Output: False

d = 10<=20
print(d)  # Output: True

# Logical Operators
x = 5
y = 10
print(x > 0 and y > 0)  # Output: True
print(x > 0 or y < 0)   # Output: True
print(not(x > 0))       # Output: False

e = True or False 
print("True or False is", True or False)  # Output: True
print("True or False is", True or True) # Output: True
print("False or False is", False or True)  # Output: True
print("False or False is", False or False)  # Output: False  

print("True and False is", True and False)  # Output: False
print("True and False is", True and True) # Output: True
print("False and False is", False and True)  # Output: False
print("False and False is", False and False)  # Output: False  

print(not(True))  # Output: False
print(not(False))  # Output: True
