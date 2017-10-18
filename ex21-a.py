def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def formula():
    print("This is the formula...enter the figures...")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    print(f"FORMULATING {a} + {b} / {c} - {d}")
    return a + b * c / d

result = formula()

print("That result is: ", result, ".")



print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# a puzzle

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")
