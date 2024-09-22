def count_vowels(str):
    vowels = "aeiou"
    vowels_dic = {}
    for ch in str:
        if ch.lower() in vowels:
            if ch not in vowels_dic.keys():
                vowels_dic[ch] = 1
            else:
                vowels_dic[ch] += 1

    print((vowels_dic))

count_vowels("a quick brown fox jumps over the lazy dog.")
