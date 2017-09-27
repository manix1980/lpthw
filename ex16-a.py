from sys import argv

script, filename = argv

print(f"Opening the file: {filename}")

target = open(filename)

print(target.read())
target.close()
