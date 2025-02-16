string = input("Enter a string: ")

if any(char.isdigit() for char in string):
    print("Contains digits")
else:
    print("No digits")
