str = "Come let us have some fun"
new_str = str.split(" ")
print(new_str)
str_length = []
def len_word(string):
    for i in string:
        a = len(i)
        str_length.append(a)

len_word(new_str)
print(str_length)
