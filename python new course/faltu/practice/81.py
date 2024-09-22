def FindOutput():
    L = "Learn and Earn"
    x = " "
    count = 1
    for i in L:
        if i in ["a","e","i","o","u"]:
            x = x + x.swapcase()
        else:
            if count %2 != 0:
                x = x + str(len(L[:count]))
            else:
                x = x + 1
    count = count + 1
    print(x)

FindOutput()