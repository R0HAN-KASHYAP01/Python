def changer(P,Q = 10):
    P = P/Q
    Q = P%Q
    return P

A = 200 
B = 20
A = changer(A,B)
print(A,B, sep = "$")
B = changer(B)
print(A,B, sep="$", end="###")

# 1. 10$20
# 2. 10$2###