# set the formatter string
formatter = "{} {} {} {}"
# print the first line and set the variables to 1,2,3,4
print(formatter.format(1,2,3,4))
# print the second line and set the variables to one, two, three, four
print(formatter.format("one", "two", "three", "four"))
# print the third line setting booleans
print(formatter.format(True, False, False, True))
# print the fourth line setting the object passing in the variable as set
print(formatter.format(formatter, formatter, formatter, formatter))
#pinrt the last section, concatenating strings
print(formatter.format (
    "To be... ",
    "or not to be...",
    "that is the question",
    "we must always match the amount of tuples in the formatter else it won't work!"
))
