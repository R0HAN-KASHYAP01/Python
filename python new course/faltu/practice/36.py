a = 15
def update(x):
    global a 
    a += 2
    if x % 2 == 0:
        a *= x
    else:
        a//=x

a = a +5
print(a,end="$")
update(5)
print(a)

# 20$4