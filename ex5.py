name = 'Mark David Ruggles'
age = 37 # not a lie
height = 190 # inches
weight = 198 # lbs
eyes = 'Blue'
teeth = 'white'
hair = 'bald'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} lbs, that is heavy.")
print("Actually that is not too heavy...")
print(f"Hes got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky

total = age + height + weight
print(f"If I add my age {age}, my height {height},and my weight {weight} I get {total}).")

my_height_in_CM = height * 2.54
my_weight_in_KG = (1/2.2) * weight
print(f"My height is {height} Inches which is equal to {my_height_in_CM}CM.")
print(f"My weight is {weight} Pounds which is equal to {my_weight_in_KG}KGS.")
