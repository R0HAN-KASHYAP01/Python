g = 0
def fun1(x,y):
    global g
    g = x +y
    return g

def fun2(m,n):
    global g
    g = m -n
    return g

k = fun1(2,3)
fun2(k,7)
print(g)