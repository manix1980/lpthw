types_of_people = 10 # setting the first variable to 10

# set a string using the types of people variable and then store it in x
x = f"There are {types_of_people} types of people"
# set a new variable to the string "binary"
binary = "Binary"
# set a second new variable to the string "don't"
do_not = "don't"
# set a string using the binary and do not variables inside the format string
y = f"Those know know {binary} and those to {do_not}."

#print out both x , y separately to the screen

print(x)
print(y)

# again print out both x and y this time inside a string and add further text
print(f"I said: {x}")
print(f"I also said: '{y}'")

# set a new variable hilarious to be fale
hilarious = "funny"
# set a new evaluation variable with a place holder for the hilarious argument
joke_evaluation = "Isn't that joke so funny?! {}"

# print out the result passing in the hilarious object as an argument
print (joke_evaluation.format(hilarious))

# concatenate two strings as part of the evaluation.

w = "This is the left side of..."
e = "a string with a right side."
# print out both sides of the string one after another.

print(w + e)
