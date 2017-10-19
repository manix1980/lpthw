print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")
    print("3. Munch all of the bears food")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")

    elif bear == "2":
        print("The bear eats your legs off. Good job")

    elif bear == "3":
        print("The bear chases you and pounds you in the ass")

    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away")

elif door == "2":
    print("You stare into the endless abyss at Cthulul's retina")
    print("1. Blueberries")
    print("2. Yellow Jacket Clothespins")
    print("3. Understanding Revolvers yelling melodies")
    print("4. I don't understand a word you are talking about muppet")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good Job")
    elif insanity == "4":
        print("Get me the hell out of here bro")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good Job")

else:
    print("You stumble around and fall on a knife and die. Good Job!")
