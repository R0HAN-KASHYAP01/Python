def change(A):
    S = 0
    for i in range(len(A)//2):
        S += (A[i]*2)
    
    return S

B = [10,11,12,30,32,34,35,38,40,2]
C = change(B)
print(C)
