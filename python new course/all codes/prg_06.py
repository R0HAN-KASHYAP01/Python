item = [int, 2, 34, 634,654,644,33,77,11,2, 6, 4]
for item in item:
    if str(item).isnumeric() and item>6:
        print(item)