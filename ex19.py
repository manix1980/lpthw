# define a new function called cheese and crackers, pass in the two parameters and print out the result

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("get a blanket.\n")

"""def apples_and_oranges():
    prompt1 = 'How many apples?'
    prompt2 = 'How many oranges'
    orange_count = int(input(prompt1))
    apple_count = int(input(prompt2))
    print(f"You have {orange_count} oranges")
    print(f"You have {apple_count} apples")
    total_fruit =  apple_count + orange_count

    print(f"You have {total_fruit} fruits!")

apples_and_oranges()

"""
# pass in numbers directly
print("We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

# or set variables and pass in the parameters using the variable names
print("OR, we can use variables from our script:")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# do the same thing using just numbers
print("We can do the math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# using the variables and modifying them on the fly
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
"""
