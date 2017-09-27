from sys import argv # import the sys package and the argv function
# set the argv variables script and filename
script, filename = argv

# print out the filename and confirm the actions we are going to perform
print(f"We're going to erase {filename}.")
print("If you don't want that. hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# get the user to confirm the actions on the file.
input("?")
print("Opening the file...")
# open the file and store the results in the target object
target = open(filename, 'w')
# truncate removes the existing lines in the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines")
# get three new lines for the files and store them in separate variables
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
output = (line1 + "\n" + line2 +"\n" + line3 + "\n")

print("I'm going to write these to the file.")

# write the new lines to open file using the .write() function

target.write(output)

# close off the file.
print("And finally we close it...")
target.close()
