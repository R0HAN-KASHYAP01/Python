ex = "google.com"
dic = {}
for num in ex:
    key = dic.keys()
    if num in key:
        dic[num] += 1

    else:
        dic[num] = 1

print(dic)