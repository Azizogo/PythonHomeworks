string = input("Enter a string: ")
vowels = "aeiou"
new_string = ''.join('*' if char in vowels else char for char in string)
print(new_string)
