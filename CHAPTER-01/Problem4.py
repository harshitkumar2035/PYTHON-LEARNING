# write a python program to print the content of a directory using os module. Search online for the function which does that.

import os   

#  select the directory whose content you want to list
directory_path = '/'

# Use the os module to list the directory content
content = os.listdir(directory_path)



# Print the content of the directory
print(f"Content of the directory '{directory_path}':")
for item in content:
    print(item)

 
