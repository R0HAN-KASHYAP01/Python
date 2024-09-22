a = 30
def call (x):
    global a 
    if a % 2 == 0:
        x+= a
    else:
        x-=a
    
    return x

x = 20
print(call(35), end = "#")
print(call(40), end = "@")