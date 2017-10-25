from sys import exit

def blue_pill():
    print("you made the right choice, here you can make it to heaven...")
    print("But only if you make choose the right beer")
    print("Do you choose #1 Pale ale or #2 Newky Broon")

    beer_choice = input("> ")

    if beer_choice == "1":
        hell()
    elif beer_choice == "2":
        heaven()
    else:
        print("you must choose a beer!")
        blue_pill()

def red_pill():
    print("Doh, you choose the red pill, that means you will be sent to hell to see the King")
    hell()

def heaven():
    print("Congratulations, welcome to heaven")
    print("You need to steal some pints to give to god, the barman is blocking the bar")
    print("We need to make him leave, to get to the bar, How many pints do you buy?")

    pint_amount = input(">")

    pints = int(pint_amount)

    if pints >= 100:
        print("Hes outta here...")
        print("God will be happy and the barman has gone to get some more barrels!")
        exit(0)
        
    elif pints >= 20 and pints <= 50:
        print("God is pissed but still not happy")
        game_over("Close, but not Enough Pints")

    else:
        game_over("No where near enough pints")

def hell():
    print("Idiot, you are in Hell because of that.")
    print("Now you are going to guess how many Dexies Danny ate yesterday")
    print("How many?")

    dexie_count = input("> ")
    dexies = int(dexie_count)

    if dexies <= 10:
        print("clearly you don't know the king!, try again")
        hell()
    elif dexies > 10 and dexies < 100:
        print("Close, but try again")
        hell()
    else:
        print("More than 100 correct, time for heaven")
        heaven()

def game_over(reason):
    print(reason, "Please try again")
    exit(0)

def start():
    print("Welcome to the matrix, neo")
    print("It's time for a choice:")
    print("Do you take the BLUE pill")
    print("or")
    print("Do you take the RED pill")

    choice = input("> ")

    if choice == "BLUE":
        blue_pill()
    elif choice == "RED":
        red_pill()
    else:
        game_over("You need to choose a pill!")
start()
