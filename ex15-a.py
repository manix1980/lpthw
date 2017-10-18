# import the argv module
from sys import argv
# set the argv variables to accept input from the user, first is the script second is filename
#script, filename = argv
# set a variable named txt and pass in the filename as a parameter to open
filename = input(" >" )
# print out hte name of the file object
print(f"Here's your file {filename}:")
# open the filename by calling the read method of the txt object
print(filename)
