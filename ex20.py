# import the argv function so we can take the input
from sys import argv

# set script and input as the two arguments
script, input_file = argv

# setup a print all function that calls the read method on the input_file, f is the object stream
def print_all(f):
    print(f.read())
# setup a rewind function that sets the position in the file to the first entry in the list 0
def rewind(f):
    f.seek(0)
# setup a print a line function which take a line number to read from and the file name f object stream
def print_a_line(line_count, f):
    print(current_line, line_count, f.readline())

# open the file name at argv using open() the input file is the second variable given on the cli
current_file = open(input_file)

# prints out the whole file first on a new line
print("First lets print the whole file:\n")

# calls the print all method with the current_file object
print_all(current_file)

print("Now lets rewind, kind of like a tape.")

# calls the rewind object on the file object stream
rewind(current_file)

print("Let's print three lines:")

# sets the stream for the input files
current_line = 1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)
