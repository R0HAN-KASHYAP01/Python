def Call(P=40,Q=20):
    P = P + Q 
    Q = P - Q 
    print(P,"@",Q)
    return(P)

R = 200
S = 100
R = Call(R,S)
print(R,"@",S)
S = Call(S)
print(R,"@",S)

''' 300@200
 300@100
120@100
300@120
'''