str = input("Enter the string:\n")
x = ['a', 'e' , 'i', 'o', 'u']
vowel = []
consonants = []
for v in str:
    if v.lower() in x:
        vowel.append(v)
    elif v.lower() not in x and v != " ":
        consonants.append(v)

print(f"Original string:\n {str}")
print(f"Vowels presented  are:\n {vowel}\n and the total number are {len(vowel)}")
print(f"Consonants presented  are:\n {consonants}\n and the total number are {len(consonants)}")

