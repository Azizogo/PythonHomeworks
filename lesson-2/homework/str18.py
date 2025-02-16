string = input("Enter a string: ")
start = input("Enter start word: ")
end = input("Enter end word: ")

if string.startswith(start) and string.endswith(end):
    print("Match")
else:
    print("No match")
