def short_sub(lst,n):
    for i in range(0,n):
        if len(lst)>4:
            lst[i] = lst[i] + lst[i]
        else:
            lst[i] = lst[i]

subject = ["CS", "Hindi", "Physics", "Chemistry", "Maths"]
short_sub(subject,5)
print(subject) 