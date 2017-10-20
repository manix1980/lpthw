def numbers_in_while(max):
    i = 0
    numbers = []

    while i < max:
        print(f"At the tops i is {i}")
        numbers.append(i)
        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The Numbers using a while loop: ")

    for num in numbers:
        print (num)

def numbers_in_for():
    numbers = []

    for i in range(0, 10):
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The Numbers using a for loop")

    for num in numbers:
        print (num)


numbers_in_while(10)
numbers_in_for()
