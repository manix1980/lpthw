print("Let's practice everything.")
print('You\'d need to know \' bout escapes with \\ that do:')
print('\nnewlines and \t tabs.')

poem = """
\tThe Lovely world
with logic so firmly planted
cannot discern \nthe needs of Lovely
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")


five = 10 - 2 + 3 - 6

# print the five variable using the format string
print(f"This should be five:{five}")

#define the formula and set the values for the amount of beans, jars and crates, return these to the secret_formula method
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# set the starting point for the formula to be 10000
start_point = 10000

# set the beans, jars and crates as the input assignment parameter for secret_formula, argv[1] is beans

jelly_beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print ("We can also do it this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
