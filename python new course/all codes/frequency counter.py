sentence = input("Enter a sentence: ").lower()
words = sentence.split()
freq = {}

# Count the frequency of each word in the sentence
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Find the word with the highest frequency
most_common_word = max(freq, key=freq.get)

print(f"The most common word in the sentence is '{most_common_word}' with a frequency of {freq[most_common_word]}.")
