vowel = "AEIOUaeiou"
vowels = consonants = uppercase = lowercase = 0

with open("Sample.txt", "r") as f:
    for line in f:
        for word in line.split():
            for char in word:
                if char in vowel:
                    vowels += 1
                elif char.isalpha():
                    consonants += 1
                    if char.islower():
                        lowercase += 1
                    elif char.isupper():
                        uppercase += 1

print(f"The number of vowels in the file is {vowels}")
print(f"The number of consonants in the file is {consonants}")
print(f"The number of uppercase letters in the file is {uppercase}")
print(f"The number of lowercase letters in the file is {lowercase}")
