string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
