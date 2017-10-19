print("""Welcome to the friends game please choose a continent:
1. for Europe.
2. for Australia.
""")

continent = input("> ")

if continent == "1":
    print("You chose Europe!")
    print("Who is your best friend in Europe?")
    print("1. Wes")
    print("2. Liam")
    print("3. Richard")
    print("4. None of those")

    europe_friend = input("> ")

    if europe_friend == "1":
        print("You choose correctly it's Wes")
    else:
        print("Your choice is incorrect")

elif continent == "2":
    print("You chose Australia!")
    print("Who is your best friend in Australia?")
    print("1. Danny")
    print("2. Nick")
    print("3. Skip")
    print("4. AP")

    oz_friend = input("> ")

    if oz_friend == "2":
        print("You choose correctly it's Nick")
    else:
        print("Your choice is incorrect")

else:
    print("Thats not a valid continent, muppet")
