sample_str = "restart"
char = sample_str[0]
new_str = sample_str.replace(char,"$")

new_str = char + new_str[1:]
print(new_str)

