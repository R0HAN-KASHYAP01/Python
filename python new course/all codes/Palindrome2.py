word = input("Enter the word: ")
reverse = word[::-1]

if word == reverse:
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} is not a palindrome")

    
