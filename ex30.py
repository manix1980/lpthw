# set the variables

people = 130
cars = 40
trucks = 45

# compare the statements and if one is true run the code under that branch, if it's false move to the next statement

if cars > people and trucks < 20:
    print("We should take the cars.")

# the first statement evaluation is false move onto the next

elif cars < people or trucks > cars:
    print("We should not take the cars.")

# if the first two statements do not match then rely on the last if statement and exit the block.

else:
    print("We can't decide.")


if trucks > cars:
    print("That's too many trucks.")

# when using elif, if the first elif is true then it will exit.

elif trucks < cars:
    print("Maybe we should take the trucks")

else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then.")
