from sys import argv # import the argv module

script, first_name, last_name  = argv # initialize the variables for the users input from argv

prompt = '# '

print(f"Hi {first_name} {last_name}, I'm the {script} script.")
print("I'd like to ask you a few questions...")
print(f"Do you like me {first_name}?")
likes = input(prompt)

print(f"Where do you live {first_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about likeing me.
You live in {lives}. Not sure where that is.
An you have a {computer} computer. Nice...
""")
