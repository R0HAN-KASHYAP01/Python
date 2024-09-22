# Comprehensions for list
ls = [i for i in range(100) if i%3==0]
print(ls)
# for dictonary
dict1 = {i:f"Item{i}" for i in range(11)}
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)