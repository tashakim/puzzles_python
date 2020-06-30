from sys import argv
"""Purpose: Simple python program to read a file specified
via argv input.
"""

script, filename = argv

print("The script name is: \n", script)

print("Let's open file: \n", filename)
txt = open(filename)
print(txt.read())