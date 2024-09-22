def changer(p,Q=10):
    p =p/Q
    Q = p%Q
    return p

A = 200
B = 20
A = changer(A,B)
print(A,B,sep='$')
B = changer(B)
print(A,B, sep='$', end='###')
