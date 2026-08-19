#  File Handling : It allows Python programs to create, read, write, and modify files .
# This is important because variable lose their data when the program ends, while files can store data permanently .
 
# Opening a File : Python uses the open() function to work with files . It is also built-in function . 

# file = open("data.txt","r")
# Here data.txt is file name and "r" is file mode

# File modes 

# r (Read) : Used to read an existing file .\
# file = open("data.txt","r")

# w (write) : Used to write data into a file . It can also overwrite existing content .
# file = open("data.txt","w")

# a (append) : Used to add new content to the end of a file . Existing content is preserved .
# file = open("data.txt","a")

# x (create) : Used to create a new file . If the file already exists Python raises an error FileExistsError . 
# file = open("data.txt","x")

# Reading a File : We can read the entire file . 

# file = open("data.txt","r")
# content = file.read()
# print(content)
# file.close()

# read() : read() reads the entire file.

# file = open("data.txt","r")
# content = file.read()

# readline() : readline() reads one line at a time from the file . Each call moves to the next line .

# with open("notes.txt","r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     print(line1)
#     print(line2)

# readlines() : Reads all the lines and returns them as a list of strings,where each element is one line (including \n at the end) 

# with open("notes.txt","r") as f:
#     lines = f.readlines()
#     print(lines)

# with : with open(...) as f : opens a file and automatically closes it when the block ends even if an error happens inside . This is the recommended way to work with files, instead of manually calling .close()

# with open("notes.txt","r") as f:
#     content = f.read()
#     print(content)

# Looping Through a File : You can directly loop over a file object - Python gives you one line at a time . This is memory-efficient for large files since it doesn't load everything at once . 

# with open("notes.txt","r") as f :
#     for line in f:
#         print(line.strip())

# write() : Writes a single string to the file . Does not add a newline automatically you must add \n yourself .

# with open("notes.txt","w") as f:
#     f.write("First entry\n")
#     f.write("Second entry\n")

# writelines() : Writes a list of strings to the file all at once . Like .write() it doesn't add newlines automatically your list items need \n included if you want line breaks . 

# lines = ["Apple\n","Banana\n","Cherry\n"]
# with open("notes.txt","w") as f:
#     f.writelines(lines)

# Handling Missing Files (FilenNotFoundError) : If you try to open a file in "r" mode and it doesn't exist, Python raises a FileNotFoundError . You can handle this with try/except 

# try :
#     with open("data.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found. Creating a new one...")
#     with open("data.txt","w") as f:
#         f.write()

# Checking If a File Exists : A safer way to check for a file's existence before trying to open it, using the os module 

# import os 
# if os.path.exists("notes.txt"):
#     print("File Exists!")
# else:
#     print("File Not Found.")

# IPO Question
