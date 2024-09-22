vowel = "aeiou"
with open("Hello.txt","r") as f:
    vowel_count = 0
    content = f.read()
    for ch in content:
        if ch in vowel:
            vowel_count += 1
        
print(vowel_count)